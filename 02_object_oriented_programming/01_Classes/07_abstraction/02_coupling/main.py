class Browser:
    def navigate(self, address):
        ip = self.__find_ip_address(address)
        html = self.__send_http_request(ip)
        print(html)

    def __send_http_request(self, ip):
        if ip is not None:
            return "<html></html>"
        else:
            return "No IP address or domain found"

    def __find_ip_address(self, address):
        if address:
            return address
        else:
            # return '127.0.0.1'
            return None

browser = Browser()
browser.navigate('127.0.0.0')
browser.navigate(None)


# A = ' '
# print(ord(A))
    
    
