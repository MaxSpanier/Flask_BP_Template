from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField, validators

class TestForm(Form):
  name = StringField("Name", [validators.DataRequired()])
  submit = SubmitField("Enter")
