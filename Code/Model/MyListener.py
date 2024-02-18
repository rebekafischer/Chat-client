from zeroconf import ServiceListener
from zeroconf import Zeroconf

class MyListener(ServiceListener):
    _userlist: list[str] = []
    
    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)

        if info:
            addresses = ["%s" % addr for addr in info.parsed_scoped_addresses()]
            self._userlist.extend(addresses)
            

    def remove_service(self, zc: 'Zeroconf', type_: str, name: str) -> None:
        print(f"Service {name} removed")

    def update_service(self, zc: 'Zeroconf', type_: str, name: str) -> None:
        print(f"Service {name} updated")