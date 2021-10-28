import urllib.request

html_res = urllib.request.urlopen('https://www.roshd.ir/')
html_content = html_res.read()
file = open("ServerFile/www.roshd.ir.html", 'w', encoding='utf-8')
file.write(html_content.decode())
file.close()