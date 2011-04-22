#!/usr/bin/env python
# coding=utf8

import wtforms.fields
import widgets

from wtforms.fields import *

class BooleanField(wtforms.fields.BooleanField):
	widget = widgets.CheckboxInput()


class CheckMultipleField(wtforms.fields.SelectMultipleField):
	widget = widgets.BlockLabelsWidget()
	option_widget = widgets.CheckboxLabeledInput()

	def __init__(self, *args, **kwargs):
		super(CheckMultipleField, self).__init__(*args, **kwargs)
		self.label = wtforms.fields.widgets.HTMLString(u'<p class="label">%s</p>' % self.label.text)


class DateField(wtforms.fields.DateField):
	widget = widgets.TextInput()


class DateTimeField(wtforms.fields.DateTimeField):
	widget = widgets.TextInput()


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
		self.label = wtforms.fields.widgets.HTMLString(u'<p class="label">%s</p>' % self.label.text)


class SubmitField(wtforms.fields.SubmitField):
	widget = widgets.SubmitInput()

	def __init__(self, *args, **kwargs):
		super(SubmitField, self).__init__(*args, **kwargs)
		self.uniform_action = kwargs.get('uniform_action', 'primary')


class TextAreaField(wtforms.fields.TextAreaField):
	widget = widgets.TextArea()


class TextField(wtforms.fields.TextField):
	widget = widgets.TextInput()
