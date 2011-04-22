#!/usr/bin/env python
# coding=utf8

import json
import re

import wtforms.validators
from wtforms.validators import *

_validator_prefix = 'wtfuf_'

def _python_to_js_regex(regex):
	flags = []
	if regex.flags | re.I: flags.append('i')
	if regex.flags | re.M: flags.append('m')

	return 'new RegExp(%s, %s)' % (json.dumps(regex.pattern), json.dumps(''.join(flags)))

class RegexJavascriptMixin(object):
	def js_validator(self, field):
		return """function(field, caption) {
			var re = %s;
			if (field.val().match(re) || field.val() == '') {
				return true;
			}
			return %s;
		}""" % (_python_to_js_regex(self.regex), json.dumps(field.gettext(self.message or 'Invalid input.')))

	def js_validator_name(self, field):
		return _validator_prefix + self.__class__.__name__


class Email(wtforms.validators.Email, RegexJavascriptMixin):
	def __init__(self, message = 'Invalid email address.'):
		super(Email, self).__init__(message)


class Regexp(wtforms.validators.Regexp, RegexJavascriptMixin):
	pass
