from flask_wtf import FlaskForm
from wtfroms import StringFiels
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min = 2, max = 20)])
