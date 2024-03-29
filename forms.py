from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField
from wtforms import StringField, TelField, IntegerField, validators
from wtforms import EmailField
from wtforms import SelectField, RadioField

class UserForm(Form):
    nombre=StringField('nombre')
    apaterno=StringField('apaterno')
    amaterno=StringField('amaterno')
    email=EmailField('email')
    edad=IntegerField('edad')

class PuntosForm(FlaskForm):
    x1 = IntegerField('x1')
    x2 = IntegerField('x2')
    y1 = IntegerField('y1')
    y2 = IntegerField('y2')
    resultado = IntegerField('resultado')



class ResistForm(Form):

    banda1 = SelectField("Banda 1", 
    choices=[(0, "Negro"), (10, "Cafe"),(20, "Rojo"),(30, "Naranja"),(40, "Amarillo"),(50, "Verde"),(60, "Azul"),(70, "Violeta"),(80, "Gris"),(90, "Blanco")])

    banda2 = SelectField("Banda 2", 
    choices=[(0, "Negro"),(1, "Cafe"),(2, "Rojo"),(3, "Naranja"),(4, "Amarillo"),(5, "Verde"),(6, "Azul"),(7, "Violeta"),(8, "Gris"),(9, "Blanco")])

    banda3 = SelectField("Banda 3", 
    choices=[(1,"Negro"),(10,"Cafe"),(100,"Rojo"),(1000,"Naranja"),(10000, "Amarillo"),(100000, "Verde"),(1000000, "Azul"),(10000000, "Violeta"),(100000000, "Gris"),(1000000000, "Blanco")])

    rbtnTol = RadioField('Tolerancia', choices=[(0.05, "Oro"), (0.1, "Plata")])


class diccionario(Form):
    espanol=StringField("espanol", validators=[
        validators.DataRequired(message='El campo es requerido')
    ])
    ingles=StringField("ingles", validators=[
        validators.DataRequired(message='El campo es requerido')
    ])

class search(Form):
    lectura = RadioField("Idioma", choices=["ingles", "espanol"])
    
    busqueda = StringField("busqueda", validators=[
        validators.DataRequired(message='El campo es requerido')
    ])
 






class ColoresResistencia():


    textco = ""
    backg = ""

    def __init__(self, c1, c2, c3, tol):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.tol = tol

    def banda1(self):
        if self.c1 == 0:
            color = "Negro"
           
        elif self.c1 == 10:
            color = "Cafe"
            
        elif self.c1 == 20:
            color = "Rojo"
           
        elif self.c1 == 30:
            color = "Naranja"
           
        elif self.c1 == 40:
            color = "Amarillo"
           
        elif self.c1 == 50:
            color = "Verde"
            
        elif self.c1 == 60:
            color = "Azul"
            
        elif self.c1 == 70:
            color = "Violeta"
            
        elif self.c1 == 80:
            color = "Gris"
            
        elif self.c1 == 90:
            color = "Blanco"
            
        
        return color
    
    def banda2(self):
        color = ""

        if self.c2 == 0:
            color = "Negro"
            
        elif self.c2 == 1:
            color = "Cafe"
            
        elif self.c2 == 2:
            color = "Rojo"
            
        elif self.c2 == 3:
            color = "Naranja"
            
        elif self.c2 == 4:
            color = "Amarillo"
            
        elif self.c2 == 5:
            color = "Verde"
            
        elif self.c2 == 6:
            color = "Azul"
            
        elif self.c2 == 7:
            color = "Violeta"
            
        elif self.c2 == 8:
            color = "Gris"
            
        elif self.c2 == 9:
            color = "Blanco"
            
        
        return color
    
    def banda3(self):
        color = ""

        if self.c3 == 1:
            color = "Negro"
            
        elif self.c3 == 10:
            color = "Cafe"
            
        elif self.c3 == 100:
            color = "Rojo"
            
        elif self.c3 == 1000:
            color = "Naranja"
           
        elif self.c3 == 10000:
            color = "Amarillo"
            
        elif self.c3 == 100000:
            color = "Verde"
            
        elif self.c3 == 1000000:
            color = "Azul"
            
        elif self.c3 == 10000000:
            color = "Violeta"
            
        elif self.c3 == 100000000:
            color = "Gris"
            
        elif self.c3 == 1000000000:
            color = "Blanco"
           
        
        return color
    
    def tolerancia(self):
        color = ""
            
        if self.tol == 0.05:
            color = "Oro"
           
        elif self.tol == 0.1:
            color = "Plata"
            
        
        return color
    

    def color1(self):
        if self.c1 == 0:
            backg = "black"
            
        elif self.c1 == 10:
            
            backg = "#4E240F"
            
        elif self.c1 == 20:
            
            backg = "red"
            textco = "black"
        elif self.c1 == 30:
            
            backg = "orangered"
            
        elif self.c1 == 40:
            
            backg = "yellow"
            
        elif self.c1 == 50:
            
            backg = "green"
            
        elif self.c1 == 60:
            
            backg = "blue"
            
        elif self.c1 == 70:
            
            backg = "#A131FF"
            
        elif self.c1 == 80:
            
            backg = "gray"
            
        elif self.c1 == 90:
            
            backg = "white"
            
        
        return backg
    
    def color2(self):
       
        if self.c2 == 0:
            
            backg = "black"
            
        elif self.c2 == 1:
            
            backg = "#4E240F"
            
        elif self.c2 == 2:
            
            backg = "red"
            
        elif self.c2 == 3:
            
            backg = "orangered"
            
        elif self.c2 == 4:
            
            backg = "yellow"
            
        elif self.c2 == 5:
            
            backg = "green"
            
        elif self.c2 == 6:
            
            backg = "blue"
            
        elif self.c2 == 7:
            
            backg = "#A131FF"
            
        elif self.c2 == 8:
            
            backg = "gray"
           
        elif self.c2 == 9:
            
            backg = "white"
            
        
        return backg
    
    def color3(self):

        if self.c3 == 1:
            
            backg = "black"
            
        elif self.c3 == 10:
            
            backg = "#4E240F"
        elif self.c3 == 100:
            
            backg = "red"
            
        elif self.c3 == 1000:
            
            backg = "orangered"
            
        elif self.c3 == 10000:
            
            backg = "yellow"
            
        elif self.c3 == 100000:
            
            backg = "green"
            
        elif self.c3 == 1000000:
            
            backg = "blue"
            
        elif self.c3 == 10000000:
           
            backg = "#A131FF"
            
        elif self.c3 == 100000000:
            
            backg = "gray"
            
        elif self.c3 == 1000000000:
            
            backg = "white"
            
        
        return backg
    
    def color4(self):
        if self.tol == 0.05:
            backg = "goldenrod"
        elif self.tol == 0.1:
            backg = "silver"
        
        return backg