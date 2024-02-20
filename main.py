from flask import Flask,render_template,request
from forms import UserForm, PuntosForm, ColoresResistencia, ResistForm, diccionario
from flask import Flask, render_template, request, send_from_directory
import os
import forms
datos = os.urandom(24)
app = Flask(__name__)
app.secret_key = 'tu_datos_aqui'


@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado",methods=["GET","POST"])
def resul():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        operacion = request.form.get("operacion")


        if operacion == "suma":
              return"El resultado de la suma es {} + {} = {}".format(num1,num2,str(int(num1)+int(num2)))
        elif operacion == "resta":
              return"El resultado de la  resta de {} - {} = {}".format(num1,num2,str(int(num1)-int(num2)))
        elif operacion == "multiplicacion":
            return"El resultado de la multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1)*int(num2)))
        elif operacion == "division":
            if num2 != 0:
                  return"El resultado de la division de {} / {} = {}".format(num1,num2,str(int(num1)/int(num2)))
        else:
            return "Error: Algo hiciste mal :/ "

@app.route("/puntos", methods=['GET', 'POST'])
def puntos():
    x1 = x2 = y1 = y2 = ''
    puntos_clase =forms.PuntosForm (request.form)
    if request.method == 'POST':
        x1 = puntos_clase.x1.data
        x2 = puntos_clase.x2.data
        y1 = puntos_clase.y1.data
        y2 = puntos_clase.y2.data
        
        resta1 = x2 - x1
        resta2 = y2 - y1

        distancia = (resta1 ** 2 + resta2 ** 2) ** 0.5

        puntos_clase.resultado.data = distancia

        print("La distancia entre los puntos es:", distancia)

        print('x1: {}'.format(x1))
        print('x2: {}'.format(x2))
        print('y1: {}'.format(y1))
        print('y2: {}'.format(y2))
        print('resultado: {}'.format(distancia))

    return render_template("distanciaPuntos.html", form=puntos_clase, x1=x1, x2=x2, y1=y1, y2=y2)        


@app.route("/dic", methods=['GET', 'POST'])
def definicion():
    espanol= ''
    ingles=''
    palabra=''
    tradduccion=''
    opciones=None
    ingresar=forms.diccionario(request.form)
    buscar=forms.search(request.form)
    if request.method == 'POST' and ingresar.validate():
        if "registrar" in request.form:
            espanol= ingresar.espanol.data
            ingles=ingresar.ingles.data
            archivo1= open('palabras.txt', 'a')
            palabra ='\n'+ espanol.lower() + '|' + ingles.lower()
            archivo1.write(palabra)
            archivo1.close()
        elif "buscar" in request.form:
            palabra = buscar.lectura.data
            opciones = buscar.busqueda.data

            with open('archivo.txt', 'r') as archivo:
                traducciones={}
                for linea in archivo:
                    linea = linea.strip()
                    partes=linea.split('|')
                    traducciones[partes[0]] = partes[1]
                    traducciones[partes[1]] =partes[0]
            if palabra.lower() in traducciones:
                tradduccion =traducciones[palabra.lower()]
            else:
                tradduccion= "Esto no esta en el diccionario"

    #palabra_espanol=forms.diccionario(request.form)
    #palabra_ingles=forms.diccionario(request.form)
    return render_template("diccionario.html", form =ingresar, espanol=espanol, ingles=ingles,
                           palabra =palabra, opciones=opciones, search=buscar,
                           respuesta=tradduccion)

if __name__ == "__main__":
    app.run(debug=True)

