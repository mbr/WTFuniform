#!/usr/bin/env python
# coding=utf8

import wtforms
import widgets

class DateField(wtforms.DateField):
	widget = widgets.TextInput()


class DateTimeField(wtforms.DateTimeField):
	widget = widgets.TextInput()


class DecimalField(wtforms.DecimalField):
	widget = widgets.TextInput()


class FileField(wtforms.FileField):
	widget = widgets.FileInput()


class FloatField(wtforms.FloatField):
	widget = widgets.TextInput()


class IntegerField(wtforms.IntegerField):
	widget = widgets.TextInput()


class PasswordField(wtforms.PasswordField):
	widget = widgets.PasswordInput()


class RadioField(wtforms.RadioField):
	widget = widgets.BlockLabelsWidget()
	option_widget = widgets.RadioInput()

	def __init__(self, *args, **kwargs):
		super(RadioField, self).__init__(*args, **kwargs)
		self.label = wtforms.widgets.HTMLString(u'<p class="label">%s</p>' % self.label.text)


class SubmitField(wtforms.SubmitField):
	widget = widgets.SubmitInput()

	def __init__(self, *args, **kwargs):
		super(SubmitField, self).__init__(*args, **kwargs)
		self.uniform_action = kwargs.get('uniform_action', 'primary')


class TextField(wtforms.TextField):
	widget = widgets.TextInput()
