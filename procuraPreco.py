import urllib.request
import time

def receberPreco(site): #retorna float com o preço
    pagina = urllib.request.urlopen(site)
    texto = pagina.read().decode("utf8")
    indexacao = (texto.find("$")) + 1
    return float((texto[indexacao : indexacao + 4]))


print("Pressione Control+C para abortar")
while True:
    precoNormal = receberPreco("http://beans.itcarlow.ie/prices.html")
    precoEspecial = receberPreco("http://beans.itcarlow.ie/prices-loyalty.html")
    mes, dia, hora, minuto, segundo = time.localtime()[1:6]  #obtém a hora em que a consulta foi feita
    print(f"Preço normal: {precoNormal}  Preço Especial: {precoEspecial} ")
    print(f"Preço obtido em {dia}/{mes}  {hora}:{minuto}:{segundo}")

    if (precoNormal < 4.70) or (precoEspecial < 4.70):
        print("*** \nCOMPRE \n***")
        time.sleep(15)

    time.sleep(2)