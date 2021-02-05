import tornado.web
import tornado.ioloop
import tornado.httpserver
import os
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
def main():
    settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),

        )
    application = tornado.web.Application([
        (r"/",basicRequestHandler),
        (r"/numeros", staticRequestHandler),
        (r"/texto", staticRequestHandler2)
        ],**settings)
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
if __name__== "__main__":
    main()
