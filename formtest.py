#!/usr/bin/env python
# coding=utf8

from wtfuniform import *
import wtfuniform.helper
import jinja2

env = jinja2.Environment(loader = jinja2.FileSystemLoader('templates'))
env.globals['render_form'] = wtfuniform.helper.render_form
env.globals['render_validator_js'] = wtfuniform.helper.render_validator_js

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
	email = TextField('Email Test', [validators.Email()], description = 'This should report an error when an invalid address is put in.')
	required_checkbox = BooleanField('Must check', [validators.Required()], description = 'A checkbox that is required')
	required_field = TextField('MustHave', [validators.Required()], description = 'A required field.')
	number = TextField('Some number', [validators.NumberRange(-5, 20)], description = 'Must be between minus five and twenty')
	field_a = TextField('Field A')
	field_b = TextField('Field B', [validators.EqualTo('field_a')], description = 'This field must be equal to Field A')
	one_of = TextField('Number between "one" and "three"', [validators.AnyOf(['one','two','three'])], description = 'Enter a number, as a word, between one and three.')
	none_of = TextField('Your favorite color, not black or white', [validators.NoneOf(['black','white'])], description = 'Enter any here, but "black" or "white"')

	# additions
	checkboxes = CheckMultipleField('Check multiple', description = 'A group of checkboxes.', choices = [('j', 'Choice J'), ('k', 'Choice K'), ('l', 'Choice L')])

form = SampleForm()

print tpl.render(form = form)
