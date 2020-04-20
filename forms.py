from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired
from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
  name =TextField("Name",[validators.Required("Please enter your name.")])
  phone=IntegerField("Phone Number")
  email= TextField("Email",[validators.Required("Please enter your email.")])
  address=TextAreaField("Address",[validators.Required("Please enter your address.")])
  firstItem=SelectField("Item1", choices=[('A',"Vitamin A"),('B1',"Vitamin B1"),('B2',"Vitamin B2"),('B3',"Vitamin B3"),('C',"Vitamin B5"),('C',"Vitamin B6"),('C',"Vitamin B12"),('C',"Vitamin C"),('C',"Vitamin D"),('C',"Vitamin E"),('C',"Vitamin K")])
  firstItemQ=SelectField("Quantity of Item1",choices=[('N','0'),('A','1'),('B','2'),('C','3'),('D','4'),('E','5')])  
  secondItem=SelectField("Item2", choices=[('A',"Vitamin A"),('B1',"Vitamin B1"),('B2',"Vitamin B2"),('B3',"Vitamin B3"),('C',"Vitamin B5"),('C',"Vitamin B6"),('C',"Vitamin B12"),('C',"Vitamin C"),('C',"Vitamin D"),('C',"Vitamin E"),('C',"Vitamin K")])
  secondItemQ=SelectField("Quantity of Item2",choices=[('N','0'),('A','1'),('B','2'),('C','3'),('D','4'),('E','5')])  
  thirdItem=SelectField("Item3", choices=[('A',"Vitamin A"),('B1',"Vitamin B1"),('B2',"Vitamin B2"),('B3',"Vitamin B3"),('C',"Vitamin B5"),('C',"Vitamin B6"),('C',"Vitamin B12"),('C',"Vitamin C"),('C',"Vitamin D"),('C',"Vitamin E"),('C',"Vitamin K")])
  thirdItemQ=SelectField("Quantity of Item3",choices=[('N','0'),('A','1'),('B','2'),('C','3'),('D','4'),('E','5')])  
  payment=RadioField("Please choose your payment method", choices=[('A','Credit card'),('B','Paypal')])
 
  submit= SubmitField("send")
  