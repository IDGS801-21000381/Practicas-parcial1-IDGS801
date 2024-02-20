from io import open

archi=open('palabrasEspaniol.txt', 'a')
archi.write('\n Palabras en Espaniol :')
archi.close()

archi2=open('palabrasIngles.txt', 'a')
archi2.write('\n Palabras en Ingles :')
archi2.close()
