import socket

class Iphdr:
    def __init__(self, tot_len, protocol, saddr, daddr):
        self.ver_len = 0x45 # 버전(4), 헤더 길이(5 = 5word * 4bytes) 
        self.tos = 0 # 서비스 타입
        self.tot_len = tot_len # 전체 길이
        self.id = 0 # 패킷 식별자
        self.frag_off = 0 # 조각화 오프셋
        self.ttl = 127 # 생존 시간
        self.protocol = protocol # 상위 프로토콜 번호
        self.check = 0 # 체크섬
        self.saddr = socket.inet_aton(saddr) # 출발지 IP(source)
        self.daddr = socket.inet_aton(daddr) # 목적지 IP(destination)

test = Iphdr(1000, 6, '10.0.0.1', '11.0.0.1')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(test), ('localhost', 2500))
