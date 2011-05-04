#!/usr/bin/env python
# coding=utf8

import cgi

from fields import FieldSet

import jinja2

class FormRenderer(object):
	env = jinja2.Environment(loader = jinja2.PackageLoader(__name__))
	templates = {}
	for tpl_name in env.list_templates(['html']):
		templates[tpl_name[:-5]] = env.get_template(tpl_name)

	def __init__(self, form, action = '.', method = 'post', mark_required = True):
	    self.form = form
	    self.mark_required = mark_required
	    self.method = method
	    self.action = action

	def _render(self, tpl, **kwargs):
		return self.templates[tpl].render(**kwargs)

	def render_errors(self, errors, title = None):
		return self._render('form_errors', errors = errors, title = title)

	def render_field(self, field, **kwargs):
		if 'HiddenField' == field.type:
			return field(**kwargs) + '\n'
		elif 'BooleanField' == field.type:
			return self._render('boolean_field', field = field, kwargs = kwargs, mark_required = self.mark_required)
		return self._render('field', field = field, kwargs = kwargs, mark_required = self.mark_required)

	def render_fieldset(self, fieldset = None, rendered_fields = []):
		if not fieldset:
			return self._render('fieldset', rendered_fields = rendered_fields, label = None, inline = False)
		return self._render('fieldset', rendered_fields = rendered_fields, label = fieldset.label.text, inline = fieldset.is_inline)

	def render_form(self, headline = None, header_content = None, prepend_validator_js = True, js_auto_init = True, error_title = None, ok_message = None, enctype = None):
		validator_js = self.render_validator_js() if prepend_validator_js else None
		js_auto_init = self.render_init_js() if js_auto_init else None

		current_fieldset = None
		current_rendered_fields = []
		fieldsets = []
		buttons = []

		for field in self.form:
			if getattr(field,'uniform_action', False):
				buttons.append(field())
			elif 'FieldSet' == field.type:
				if current_fieldset or current_rendered_fields:
					fieldsets.append(self.render_fieldset(current_fieldset, current_rendered_fields))
				current_fieldset = field
				current_rendered_fields = []
			else:
				current_rendered_fields.append(self.render_field(field))
		fieldsets.append(self.render_fieldset(current_fieldset, current_rendered_fields))

		return self._render('form', action = self.action,
		                            method = self.method,
		                            form = self.form,
		                            headline = headline,
		                            header_content = header_content,
		                            fieldsets = fieldsets,
		                            buttons = buttons,
		                            enctype = enctype,
		                            validator_js = validator_js,
		                            js_auto_init = js_auto_init,
		                            error_title = error_title,
		                            ok_message = ok_message)

	def render_init_js(self):
	    return u"""<script type="text/javascript">$(document).ready"""\
	           u"""(function(){ if not(window._wtforms_uniform_initialized) {
	           $('form.%s').uniForm(); window._wtforms_uniform_initialized =
	           true; }});</script>"""

	def render_validator_js(self):
		js = []
		for field in self.form:
			for validator in field.validators:
				if hasattr(validator, 'js_validator'):
					js.append("window['%s'] = %s;" % (validator.js_validator_name(field), validator.js_validator(self.form, field)))

		return '\n'.join(js);
