#!/usr/bin/env python
# coding=utf8

import wtforms.fields
import widgets

from wtforms.fields import *

# FIXME: This is a hackish solution, but do we really
#        want to monkey patch the metaclass just for this?
class FieldSet(wtforms.fields.Field):
	widget = lambda _1,_2: ''

	def __init__(self, title = None, inline = False, **kwargs):
		super(FieldSet, self).__init__(title, **kwargs)
		self.is_inline = inline


class PLabel(wtforms.fields.Label):
	def __call__(self, text = None, **kwargs):
		return wtforms.widgets.HTMLString(u'<p class="label">%s</p>' % (text or self.text))


class BooleanField(wtforms.fields.BooleanField):
	widget = widgets.CheckboxInput()


class CheckMultipleField(wtforms.fields.SelectMultipleField):
	widget = widgets.BlockLabelsWidget()
	option_widget = widgets.CheckboxLabeledInput()

	def __init__(self, *args, **kwargs):
		super(CheckMultipleField, self).__init__(*args, **kwargs)
		self.label = PLabel(self.id, kwargs.get('label', u'') or kwargs.get('_name', None).replace('_', ' ').title())


class DateField(wtforms.fields.DateField):
	widget = widgets.TextInput(uniform_extra_classes = ['dateInput'])


class DateTimeField(wtforms.fields.DateTimeField):
	widget = widgets.TextInput(uniform_extra_classes = ['dateTimeInput'])


class DecimalField(wtforms.fields.DecimalField):
	widget = widgets.TextInput()


class FileField(wtforms.fields.FileField):
	widget = widgets.FileInput()


class FloatField(wtforms.fields.FloatField):
	widget = widgets.TextInput()


class IntegerField(wtforms.fields.IntegerField):
	widget = widgets.TextInput()


class PasswordField(wtforms.fields.PasswordField):
	widget = widgets.PasswordInput()


class RadioField(wtforms.fields.RadioField):
	widget = widgets.BlockLabelsWidget()
	option_widget = widgets.RadioLabeledInput()

	def __init__(self, *args, **kwargs):
		super(RadioField, self).__init__(*args, **kwargs)
		self.label = PLabel(self.id, kwargs.get('label', u'') or kwargs.get('_name', None).replace('_', ' ').title())


class SubmitField(wtforms.fields.SubmitField):
	widget = widgets.SubmitInput()

	def __init__(self, *args, **kwargs):
		super(SubmitField, self).__init__(*args, **kwargs)
		self.uniform_action = kwargs.get('uniform_action', 'primary')


class TextAreaField(wtforms.fields.TextAreaField):
	widget = widgets.TextArea()


class TextField(wtforms.fields.TextField):
	widget = widgets.TextInput()
