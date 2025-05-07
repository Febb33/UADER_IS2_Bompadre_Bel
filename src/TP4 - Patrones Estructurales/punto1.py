
import os

class Ping:
    def execute(self, ip: str):
        if ip.startswith("192."):
            os.system(f"ping -n 10 {ip}" if os.name == 'nt' else f"ping -c 10 {ip}")
        else:
            print("Dirección IP no permitida para este método.")

    def executefree(self, ip: str):
        os.system(f"ping -n 10 {ip}" if os.name == 'nt' else f"ping -c 10 {ip}")

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip: str):
        if ip == "192.168.0.254":
            print("Redireccionando a www.google.com")
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip)



if __name__ == "__main__":
    proxy = PingProxy()

    
    proxy.execute("192.168.0.254")

    
    proxy.execute("192.168.1.1")

    
    proxy.execute("8.8.8.8")
