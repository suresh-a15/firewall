from fwall import Firewall

#testing func
def main():
    fw = Firewall("./fwall.csv")
    print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
    print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"))
    print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
    print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
    print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))

    print(fw.accept_packet("outbound", "tcp", 25750, "192.168.10.11"))
    print(fw.accept_packet("inbound", "tcp", 100, "1.1.1.1"))
    print(fw.accept_packet("inbound", "tcp", 100, "2.2.2.2"))
    print(fw.accept_packet("inbound", "tcp", 100, "1.1.1.2"))

    print(fw.accept_packet("inbound", "udp", 100, "1.1.1.2"))
    print(fw.accept_packet("inbound", "udp", 1, "0.0.0.0"))
    print(fw.accept_packet("inbound", "udp", 65535, "255.255.255.255"))

main()


