#!/usr/bin/env python2
import binascii
import os
import struct
import sys

# data.bin header from Super Mario World
orig_header = binascii.unhexlify("000100001090090030000000500000006000000060000800C08E090000000000109009004B54522D55414145000000003C00000800608E0100500100001110027814000000000000000000000000000003000000010000000000000000000000")

helptext = """usage: snesinject.py [options] <SNES ROM>

options:
  --hirom          - use HiROM
  --lorom          - use LoROM
  at least one of the above is required

  --dsp            - use DSP

  --output=<name>  - output filename
                     default is data.bin"""

if len(sys.argv) < 2:
    print(helptext)
    sys.exit(1)

hirom = "--hirom" in sys.argv
lorom = "--lorom" in sys.argv
if not hirom ^ lorom:
    print("! need one --hirom or --lorom")
    sys.exit(1)

dsp = "--dsp" in sys.argv

rom_name = ""
output_name = "data.bin"
for arg in sys.argv[1:]:
    if arg[:2] != "--":
        if rom_name != "":
            print("! only one ROM is used")
            sys.exit(1)
        rom_name = arg
    elif arg[:9] == "--output=":
        output_name = arg[9:]

if not os.path.isfile(rom_name):
    print("! ROM file doesn't exist")
    sys.exit(1)

rom_filesize = os.path.getsize(rom_name)
databin_filesize_hex = struct.pack("<i", rom_filesize + len(orig_header))
#print(binascii.hexlify(databin_filesize_hex))

databin = open(output_name, "wb")
rom = open(rom_name, "rb")
databin.write(orig_header + rom.read())
rom.close()
# thanks Nintendo!
databin.seek(0x4)
databin.write(databin_filesize_hex)
databin.seek(0x14)
databin.write(databin_filesize_hex)
databin.seek(0x18)
databin.write(databin_filesize_hex)
databin.seek(0x20)
databin.write(databin_filesize_hex)
if dsp:
    databin.seek(0x3D)
    databin.write('\xBA')
databin.seek(0x41)
if lorom:
    databin.write('\x14')
elif hirom:
    databin.write('\x15')
else:
    print("! this error shouldn't have happened (unknown HiROM/LoROM)")
    databin.close()
    sys.exit(1)
# TODO: convert PAL to NTSC (LoROM: 0x7FD9 should be 0x01 to be NTSC)
databin.seek(0x33)
databin.write(chr((rom_filesize / 0x80000) * 0x8))

databin.close()
