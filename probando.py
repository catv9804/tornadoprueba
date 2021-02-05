
##icontentlist=[]
##file= open("numeros.txt", "r")
##content = file.read()
##print(content)
##content_list= content.split(",")
##file.close()
##print(content_list)
##for i in range(len(content_list)):
##    icontentlist.append(int(content_list[i]))
##print(icontentlist)
##Salida=sorted(icontentlist, reverse=True)
##print(Salida)

file= open("texto.txt", "r")
content = file.read()
mayusculas = len([c for c in content if c.isupper()])
cadena=len(content)
cadenasinespacio = str(content).replace(" ", "")
espacios=cadena-len(cadenasinespacio)

    
print("el total de espacios es :", espacios, "y de mayusculas es: ", mayusculas)
