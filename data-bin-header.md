pointers and sizes seem to be little-endian?

Offset | Size | Description
--- | --- | ---
0x4 | 0x4 | File length
0x10 | 0x4 | ROM starting offset
0x14 | 0x4 | ROM ending offset
0x18 | 0x4 | Footer offset
0x20 | 0x4 | File length
0x24 | 0x8 | Title ID (e.g. `KTR-UAAE`)
0x33 | 0x1 | ROM size indicator
0x3D | 0x1 | Not fully known?; 0xBA enables DSP (Super Mario Kart uses this apparently)
0x41 | 0x1 | Not fully known?; 0x14 = LoROM, 0x15 = HiROM

ROM size indicator values:

Size(bytes) | Size(bits) | Value
--- | --- | ---
512kib | 4mbit | 0x08
1mib | 8mbit | 0x10
1.5mib | 12mbit | 0x18
2mib | 16mbit | 0x20
2.5mib | 20mbit | 0x28
3mib | 24mbit | 0x30
3.5mib | 28mbit | 0x38
4mib | 32mbit | 0x40
4.5mib | 36mbit | 0x48
5mib | 40mbit | 0x50
5.5mib | 44mbit | 0x58
6mib | 48mbit | 0x60
