class IPAddress:
    def __init__(self, ipaddress):
        if isinstance(ipaddress, str):
            sp = ipaddress.split(".")
            sp = [int(x) for x in sp]
        else:
            sp = list(ipaddress)

        if len(sp) != 4:
            raise ValueError("IP должен содержать ровно 4 числа")
        
        for i in sp:
            if i < 0 or i > 255:
                raise ValueError("Каждое число IP должно быть от 0 до 255")
        self.ipaddress = ".".join(str(x) for x in sp)
    def __str__(self):
         return self.ipaddress
    def __repr__(self):
        return  f"IPAddress({self.ipaddress})"
    
    
ip1 = IPAddress("15.56.48.79")
ip2 = IPAddress([245,56,12,7])

print(ip1)        
print(ip2)

print(repr(ip1))   
print(repr(ip2))