#!/usr/bin/env python
# coding=utf8

def render_field(field, **kwargs):
	return u"""<div class="ctrlHolder">
      %s
      %s
      <p class="formHint">%s</p>
    </div>
    """ % (field.label, field(**kwargs), field.description)


def render_form(form, action = '.', use_inline = False, prepend_validator_js = True):
	chunks = []
	if prepend_validator_js:
		chunks.append('<script type="text/javascript">')
		chunks.append(render_validator_js(form))
		chunks.append('</script>')
	chunks.append(u"""<form action="%s" class="uniForm">
  <fieldset%s>
  	""" % (action,' class="inlineLabels"' if use_inline else ''))
  	buttons = []

  	for field in form:
  		if getattr(field,'uniform_action', False):
  			buttons.append(field())
  		else:
  			chunks.append(render_field(field))

	chunks.append(u"""
    <div class="buttonHolder">
    	%s
    </div>
	""" % (u''.join(buttons)))

	chunks.append(u"""
  </fieldset>
</form>
  """)

  	return u''.join(chunks)


def render_validator_js(form):
	js = []
	for field in form:
		for validator in field.validators:
			if hasattr(validator, 'js_validator'):
				js.append("window['%s'] = %s;" % (validator.js_validator_name(field), validator.js_validator(form, field)))

	return '\n'.join(js);
