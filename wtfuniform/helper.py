#!/usr/bin/env python
# coding=utf8

import cgi

from fields import FieldSet

def render_field(field, **kwargs):
	if 'HiddenField' == field.type:
		return field(**kwargs) + '\n'
	return u"""<div class="ctrlHolder%s">
      %s
      %s
      <p class="formHint">%s</p>
    </div>
    """ % (' error' if field.errors else '',
           field.label('<em>*</em> %s' % field.label.text if field.flags.required else None),
           field(**kwargs),
           field.description
          )


def render_fieldset_end(fieldset):
  	return u'   </fieldset>'


def render_fieldset_start(fieldset):
  	chunks = []
  	chunks.append(u'   <fieldset%s>' % (' class="inlineLabels"' if getattr(fieldset, 'is_inline', None) else ''))
  	if getattr(fieldset, 'label', None):
  		chunks.append(u'\n      <h3>%s</h3>' % fieldset.label.text)

  	return ''.join(chunks)


def render_errors(errors, title = None):
	chunks = []
	chunks.append(u'     <div id="errorMsg">')
	if title: chunks.append(u'        <h3>%s</h3>' % title)
	chunks.append(u'       <ol>')
	for error in errors:
		chunks.append(u'          <li>%s</li>' % (error,))

	chunks.append(u'       </ol>')
	chunks.append(u'      </div>')

	return u'\n'.join(chunks)


def render_form(form, action = '.', headline = None, header_content = None, prepend_validator_js = True, errors = 'top', error_title = None, ok_message = None):
	chunks = []
	if prepend_validator_js:
		chunks.append('<script type="text/javascript">')
		chunks.append(render_validator_js(form))
		chunks.append('</script>')

	chunks.append(u"""<form action="%s" class="uniForm">\n""" % (action,));
	if headline or header_content:
		chunks.append(render_header(headline, header_content))

	error_msgs = []
	if 'top' == errors and form.errors:
		for field_name, field_errors in form.errors.iteritems():
			for error in field_errors:
				# FIXME: This makes it impossible to use HTML in error messages,
				#        but we need to prevent XSS from user input on GET requests.
				error_msgs.append('<span class="errorFieldName">%s</span>: %s' % (cgi.escape(form[field_name].label.text), cgi.escape(error)))
	chunks.append(render_errors(error_msgs, error_title))

	if ok_message:
		chunks.append(render_ok(ok_message))

	current_fieldset = None

  	buttons = []
  	for field in form:
  		if getattr(field,'uniform_action', False):
  			buttons.append(field())
  		elif 'FieldSet' == field.type:
  			if current_fieldset:
  				chunks.append(render_fieldset_end(current_fieldset))
  			current_fieldset = field
  			chunks.append(render_fieldset_start(current_fieldset))
  		else:
  			if not current_fieldset:
  				current_fieldset = FieldSet()
  				chunks.append(render_fieldset_start(current_fieldset))
  			chunks.append(render_field(field, class_ = 'error' if True else None))

	chunks.append(u"""
    <div class="buttonHolder">
    	%s
    </div>
	""" % (u''.join(buttons)))

  	if current_fieldset: chunks.append(render_fieldset_end(current_fieldset))
	chunks.append(u""" </form>""")

  	return u''.join(chunks)


def render_header(headline, content):
	return u"""       <div class="header">
        <h2>%s</h2>
        <p>%s</p>
      </div>""" % (headline, content)


def render_ok(message):
	return u"""      <div id="okMsg">
        <p>
          %s
        </p>
      </div>""" % (message,)


def render_validator_js(form):
	js = []
	for field in form:
		for validator in field.validators:
			if hasattr(validator, 'js_validator'):
				js.append("window['%s'] = %s;" % (validator.js_validator_name(field), validator.js_validator(form, field)))

	return '\n'.join(js);
