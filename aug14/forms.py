from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class VoterForm(FlaskForm):
    # name = field(label)
    fullname = StringField("Full name",validators=[
        DataRequired(message="full name must be exists"),
        Regexp(r"^[A-Za-z ]{3,50}$", message="Invalid name")
    ])
    age = StringField("Age", validators=[
        DataRequired(message="age must exists"),
        Regexp(r"^[0-9]{1,2}$",message="Invalid age")
    ])
    email = EmailField("Email",validators=[
        DataRequired(message="Exmail must exists"),
        Regexp(r"[a-z]{3,20}@[a-z]{2,}\.[a-z]{2,}", message="invalid email")
    ])
    aadhaar = StringField("Aadhaar",validators=[
        DataRequired(message="Aadhaar is mandate"),
        Regexp(r"^[0-9]{12}$",message="Invalid aadhaar")
    ])
    gender = RadioField("Gender",choices=[
        # (actual, presentable content)
        ('male',"Male"),
        ('female',"FeMale"),
        ('other',"Others")
    ], validators=[
        DataRequired(message="Gender must be selected")
    ])
    constituency = SelectField("Select Constituency",choices=[
        ('karkala',"Karkala"),
        ('moodbidri',"Moodbidri"),
        ('udupi',"Udupi"),
        ('manglore',"Mangaluru"),
    ])
    declaration = FileField("Upload Self declaration document", validators=[
        DataRequired(message="File must be uploaded")
    ])
    submit = SubmitField("Apply")