import sys
import struct

f = open(sys.argv[1], 'rb')
offset=0

#while True:
data = f.read(512)

print("Is MBR? ", hex(struct.unpack_from("<H", data, 0x1FE)[0]))
print()

#partition 1
print("Partition 1")
print("Boot? ", hex(struct.unpack_from("<b", data, 0x1BE)[0]))
print("LBA Start: ", hex(struct.unpack_from("<l", data, 0x1C6)[0]))
print("Partition Sector number: ", hex(struct.unpack_from("<l", data, 0x1CA)[0]))
print()

#partition 2
print("Partition 2")
print("Boot? ", hex(struct.unpack_from("<b", data, 0x1CE)[0]))
print("LBA Start: ", hex(struct.unpack_from("<l", data, 0x1D6)[0]))
print("Partition Sector number: ", hex(struct.unpack_from("<l", data, 0x1DA)[0]))
print()

#partition 3
print("Partition 3")
print("Boot? ", hex(struct.unpack_from("<b", data, 0x1DE)[0]))
print("LBA Start: ", hex(struct.unpack_from("<l", data, 0x1E6)[0]))
print("Partition Sector number: ", hex(struct.unpack_from("<l", data, 0x1EA)[0]))
print()

#partition 4
print("Partition 4")
print("Boot? ", hex(struct.unpack_from("<b", data, 0x1EE)[0]))
print("LBA Start: ", hex(struct.unpack_from("<l", data, 0x1F6)[0]))
print("Partition Sector number: ", hex(struct.unpack_from("<l", data, 0x1FA)[0]))
print()	
