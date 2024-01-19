class StartMessage:

    import netifaces as ni
    ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
    print(ip)

    name = input("Geben Sie ihren Namen ein")

    def __init__(self, name, ip):
        self.name = name #instance variable
        self.ip = ip #instance variable 

