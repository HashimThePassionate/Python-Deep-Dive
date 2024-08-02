class Browser:
    def navigate(self, address: str):
        ip = self.__find_ip_address(address)
        if ip is None:
            return "No IP address or domain found"
        html = self.__send_http_request(ip)
        return html

    def __find_ip_address(self, ip: str) -> str:
        if not ip:
            return None
        return ip

    def __send_http_request(self, ip: str):
        if self.__is_valid_ip(ip) or ip == 'localhost':
            return """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <h1>Welcome to the website</h1>
            </body>
            </html>"""
        else:
            return "404 Not Found"


    def __is_valid_ip(self, ip: str) -> bool:
        parts = ip.split('.')
        if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
            return True
        return False

# Testing the code
nav = Browser()
print(nav.navigate('localhost'))  # Should return HTML content
print(nav.navigate(''))           # Should return "No IP address or domain found"
print(nav.navigate(None))         # Should return "No IP address or domain found"
print(nav.navigate('127.0.0.1'))  # Should return HTML content for the IP # Should return HTML content for a valid domain
print(nav.navigate('invalid-ip'))  # Should return "404 Not Found"
