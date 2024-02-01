from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, TelField, IntegerField
from wtforms import EmailField

from wtforms.validators import DataRequired, Email


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
