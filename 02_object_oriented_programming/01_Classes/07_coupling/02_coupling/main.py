class Browser:
    def navigate(self, address):
        ip = self.__find_ip_address(address)
        html = self.__send_http_request(ip)
        print(html)

    def __send_http_request(self, ip):
        return "<html></html>"

    def __find_ip_address(self, address):
        if address:
            return address
        else:
            return '127.0.0.1'

if __name__ == "__main__":
    browser = Browser()
    browser.navigate('127.0.0.0')
    
    
