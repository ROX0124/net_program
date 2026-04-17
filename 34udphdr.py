import struct
import binascii
import socket

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length   = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)
        return packed

def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

def getSrcPort(unpacked_udpheader):  return unpacked_udpheader[0]
def getDstPort(unpacked_udpheader):  return unpacked_udpheader[1]
def getLength(unpacked_udpheader):   return unpacked_udpheader[2]
def getChecksum(unpacked_udpheader): return unpacked_udpheader[3]

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'
    .format(getSrcPort(unpacked_udphdr), getDstPort(unpacked_udphdr),
            getLength(unpacked_udphdr), getChecksum(unpacked_udphdr)))
