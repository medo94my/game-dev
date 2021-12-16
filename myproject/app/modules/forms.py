from wtforms import Form, StringField, TextAreaField, PasswordField, validators


class RegisterForm(Form):
    name = StringField('Name', [validators.length(min=1, max=50)])
    username = StringField('Username', [validators.length(min=4, max=25)])
    email = StringField('Email', [validators.length(min=4, max=50)])
    password = PasswordField('Password',
                             [validators.DataRequired(),
                              validators.EqualTo('confirm', message='password do not match')])
    confirm = PasswordField('Confirm Password')
class LoginForm(Form):
    username = StringField('Username', [validators.length(min=4, max=25)])
    password = PasswordField('Password',
                             [validators.DataRequired(),validators.length(min=8)])



class GameForm(Form):
    title = StringField('Title', [validators.length(min=6, max=200)])