#!/usr/bin/env python
# coding=utf8

def render_field(field, **kwargs):
	return u"""<div class="ctrlHolder">
      %s
      %s
      <p class="formHint">%s</p>
    </div>
    """ % (field.label, field(**kwargs), field.description)


def render_form(form, action = '.', headline = None, header_content = None, use_inline = False, prepend_validator_js = True, render_errors = 'top'):
	chunks = []
	if prepend_validator_js:
		chunks.append('<script type="text/javascript">')
		chunks.append(render_validator_js(form))
		chunks.append('</script>')

	chunks.append(u"""<form action="%s" class="uniForm">\n""" % (action,));
	if headline or header_content:
		chunks.append(render_header(headline, header_content))

	chunks.append(u""" <fieldset%s>\n""" % ' class="inlineLabels"' if use_inline else '')

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


def render_header(headline, content):
	return u"""       <div class="header">
        <h2>%s</h2>
        <p>%s</p>
      </div>""" % (headline, content)


def render_validator_js(form):
	js = []
	for field in form:
		for validator in field.validators:
			if hasattr(validator, 'js_validator'):
				js.append("window['%s'] = %s;" % (validator.js_validator_name(field), validator.js_validator(form, field)))

	return '\n'.join(js);
