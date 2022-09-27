import urllib.request
import time

def receberPreco(site):
    pagina = urllib.request.urlopen(site)
    texto  = pagina.read().decode("utf8")
    indexacao = (texto.find("$"))+1
    return float((texto[indexacao:indexacao+4]))

print(receberPreco("http://beans.itcarlow.ie/prices.html"))
print(receberPreco("http://beans.itcarlow.ie/prices-loyalty.html"))

while True:
    print("Pressione Control+C para abortar")
    precoNormal = receberPreco("http://beans.itcarlow.ie/prices.html")
    precoEspecial = receberPreco("http://beans.itcarlow.ie/prices-loyalty.html")

    if(precoNormal < 4.70) or (precoEspecial < 4.70): 
        print("COMPRE COMPRE COMPRE")
        time.sleep(15)

    time.sleep(2)