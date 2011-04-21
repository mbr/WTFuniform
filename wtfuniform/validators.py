#!/usr/bin/env python
# coding=utf8

from wtforms.validators import Email as WTFEmail

class Email(WTFEmail):
	field_flags = ('valid_email',)
