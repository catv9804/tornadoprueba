import tornado.web
import tornado.ioloop
import os
import logging
import tornado.httpserver
import tornado.options
from tornado.options import define, options

define("environment", default="development", help="Pick you environment", type=str)
define("site_title", default="Tornado Example", help="Site Title", type=str)
define("cookie_secret", default="sooooooosecret", help="Your secret cookie dough", type=str)
define("port", default="8000", help="Listening port", type=str)
class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        
        icontentlist=[]
        file= open("numeros.txt", "r")
        content = file.read()
        self.write("Los numeros leidos del archivo txt son: ")
        self.write("<br>")
        self.write(str(content))
        print(content)
        content_list= content.split(",")
        file.close()
        print(content_list)
        for i in range(len(content_list)):
            icontentlist.append(int(content_list[i]))
        print(icontentlist)
        Salida=sorted(icontentlist, reverse=True)
        print(Salida)
        self.write("<br>")
        self.write("<br>")
        self.write("Los numeros ordenados son: ")
        self.write("<br>")
        self.write(str(Salida))
        self.render("numeros.html")
    
class staticRequestHandler2(tornado.web.RequestHandler):
    def get(self):
        file= open("texto.txt", "r")
        content = file.read()
        mayusculas = len([c for c in content if c.isupper()])
        cadena=len(content)
        cadenasinespacio = str(content).replace(" ", "")
        espacios=cadena-len(cadenasinespacio)
        suma=espacios+mayusculas
        self.write("el total de espacios es :")
        self.write(str(espacios))
        self.write("<br>")
        self.write("y de mayusculas es: ")
        self.write(str(mayusculas))
        self.write("<br>")
        self.write("Para un total de :")
        self.write(str(suma))
        
        self.render("texto.html")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
           (r"/", basicRequestHandler),
           (r"/numeros", staticRequestHandler),
           (r"/texto", staticRequestHandler2)
        ]
        settings = dict(
            site_title=options.site_title,
            cookie_secret=options.cookie_secret,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    tornado.options.parse_command_line()
    print "Server listening on port " + str(options.port)
    logging.getLogger().setLevel(logging.DEBUG)
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
"""
if __name__== "__main__":
    app=tornado.web.Application([
        (r"/",basicRequestHandler),
        (r"/numeros", staticRequestHandler),
        (r"/texto", staticRequestHandler2)
        ])
    app.listen(80)
    print("escuchando por el puerto 80")
    tornado.ioloop.IOLoop.current().start()
"""
