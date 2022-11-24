from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, SubmitField, validators
from wtforms.validators import DataRequired

class TestForm(FlaskForm):
  name = StringField("Name", validators=[DataRequired()])
 
