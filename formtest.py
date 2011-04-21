#!/usr/bin/env python
# coding=utf8

from wtforms import *
from wtforms.validators import Required, Email, NumberRange
#from wtfuniform import *
import jinja2

env = jinja2.Environment(loader = jinja2.FileSystemLoader('templates'))

tpl = env.get_template('formtest.html')

class SampleForm(Form):
	boolean_field = BooleanField('BooleanField', description = 'A BooleanField example')
	date_field = DateField('DateField', description = 'A DateField example')
	date_time_field = DateTimeField('DateTimeField', description = 'A DateTimeField example')
	decimal_field = DecimalField('DecimalField', description = 'A DecimalField example')
	file_field = FileField('FileField', description = 'A FileField example')
	float_field = FloatField('FloatField', description = 'A FloatField example')
	hidden_field = HiddenField('HiddenField', description = 'A HiddenField example')
	integer_field = IntegerField('IntegerField', description = 'A IntegerField example')
	password_field  = PasswordField('PasswordField', description = 'A PasswordField example')
	radio_field = RadioField('RadioField', description = 'A RadioField example', choices = [('a', 'Choice A'), ('b', 'Choice B'), ('c', 'Choice C')])
	select_field = SelectField('SelectField', description = 'A SelectField example', choices = [('d', 'Choice D'), ('e', 'Choice E'), ('f', 'Choice F')])
	select_multiple_field = SelectMultipleField('SelectMultipleField', description = 'A SelectMultipleField example', choices = [('g', 'Choice G'), ('h', 'Choice H'), ('i', 'Choice I')])
	submit_field = SubmitField('SubmitField', description = 'A SubmitField example')
	text_area_field = TextAreaField('TextAreaField', description = 'A TextAreaField example')
	text_field = TextField('TextField', description = 'A TextField example')

	# check client-side validators
	#username = TextField('EMAIL', [Required(), Email()], default = 'def')
	#username_uniform = TextField('Different widget', default = 'def')
	#a_required_field = TextField('MustHave', [Required()], default = 'def')
	#number = TextField('Some number', [NumberRange(-5, 20)])

form = SampleForm()

print tpl.render(form = form)
