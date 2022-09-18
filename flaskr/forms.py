from wtforms import Form, BooleanField, StringField, PasswordField, validators

class TestForm(Form):
  name = StringField("Name", [validators.DataRequired()]
