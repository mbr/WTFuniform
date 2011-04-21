#!/usr/bin/env python
# coding=utf8

import wtforms.validators
from wtforms.validators import *

class Email(wtforms.validators.Email):
	field_flags = ('valid_email',)
