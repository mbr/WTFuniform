#!/usr/bin/env python
# coding=utf8

import wtforms.widgets
from wtforms.widgets import *

def _pop_classes(d):
	return (d.pop('class', '') or d.pop('class_', '')).split()


def get_validation_classes(field):
	c = []

	if field.flags.required:
		c.append('required')

	# number range
	for validator in field.validators:
		if hasattr(validator, 'min'):
			c.append('validateMin')
			c.append('val-%d' % validator.min)
		if hasattr(validator, 'max'):
			c.append('validateMax')
			c.append('val-%d' % validator.max)
		if hasattr(validator, 'js_validator'):
			c.append('validateCallback')
			c.append(validator.js_validator_name(field))

	return c


class BlockLabelsWidget(object):
	def __call__(self, field, **kwargs):
		classes = _pop_classes(kwargs)
		classes.append('blockLabels')
		kwargs['class'] = ' '.join(classes)

		html = [u'<ul %s>' % (wtforms.widgets.html_params(**kwargs))]
		for subfield in field:
			s = subfield()
			html.append(u'<li>%s</li>' % (subfield()))
		html.append(u'</ul>')
		return wtforms.widgets.HTMLString(u'\n'.join(html))


class CheckboxInput(wtforms.widgets.CheckboxInput):
	def __call__(self, field, **kwargs):
		classes = _pop_classes(kwargs)
		classes += get_validation_classes(field)
		kwargs['class'] = ' '.join(classes)
		return super(CheckboxInput, self).__call__(field, **kwargs)


class CheckboxLabeledInput(CheckboxInput):
	def __call__(self, field, **kwargs):
		checkbox = super(CheckboxLabeledInput, self).__call__(field, **kwargs)

		return wtforms.widgets.HTMLString(u'<label %s>%s %s</label>'  % (wtforms.widgets.html_params(for_ = field.id), checkbox, field.label.text))


class FileInput(wtforms.widgets.FileInput):
	def __call__(self, field, **kwargs):
		classes = _pop_classes(kwargs)
		classes.append('fileUpload')
		classes += get_validation_classes(field)
		kwargs['class'] = ' '.join(classes)
		return super(FileInput, self).__call__(field, **kwargs)


class UnorderedListWidget(wtforms.widgets.ListWidget):
	def __init__(self, alternate = False):
		self.alternate = True

	def __call__(self, field, **kwargs):
		classes = _pop_classes(kwargs)
		kwargs['class'] = ' '.join(classes)

		html = [u'<ul %s>' % (wtforms.widgets.html_params(**kwargs))]
		for subfield in field:
			s = subfield.label('%s %s' % (subfield.label.text, subfield(**kwargs)))
			html.append(u'<li>%s</li>' % (s))
		html.append(u'</ul>')
		return wtforms.widgets.HTMLString(u'\n'.join(html))



class PasswordInput(wtforms.widgets.PasswordInput):
	def __call__(self, field, **kwargs):
		classes = _pop_classes(kwargs)
		classes.append('textInput')
		classes += get_validation_classes(field)
		kwargs['class'] = ' '.join(classes)
		return super(PasswordInput, self).__call__(field, **kwargs)


class RadioLabeledInput(wtforms.widgets.RadioInput):
	def __call__(self, field, **kwargs):
		radio = super(RadioInput, self).__call__(field, **kwargs)
		return wtforms.widgets.HTMLString(u'<label %s>%s %s</label>'  % (wtforms.widgets.html_params(for_ = field.id), radio, field.label.text))


class SubmitInput(wtforms.widgets.SubmitInput):
	def __call__(self, field, **kwargs):
		classes = _pop_classes(kwargs)
		classes.append(field.uniform_action + 'Action')
		kwargs['class'] = ' '.join(classes)
		return super(SubmitInput, self).__call__(field, **kwargs)


class TextArea(wtforms.widgets.TextArea):
	def __call__(self, field, **kwargs):
		classes = _pop_classes(kwargs)
		classes += get_validation_classes(field)
		kwargs['class'] = ' '.join(classes)
		return super(TextArea, self).__call__(field, **kwargs)


class TextInput(wtforms.widgets.TextInput):
	def __init__(self, *args, **kwargs):
		self.uniform_extra_classes = ['textInput'] + kwargs.pop('uniform_extra_classes', [])
		super(TextInput, self).__init__(*args, **kwargs)

	def __call__(self, field, **kwargs):
		classes = _pop_classes(kwargs)
		classes += self.uniform_extra_classes
		classes += get_validation_classes(field)
		kwargs['class'] = ' '.join(classes)
		return super(TextInput, self).__call__(field, **kwargs)
