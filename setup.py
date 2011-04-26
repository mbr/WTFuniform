#!/usr/bin/env python
# coding=utf8

from distutils.core import setup

setup(name='WTFuniform',
      version='0.1',
      description='Use WTForms to output uni-form enabled forms. Extends wtforms and supplies some HTML-generating functions.',
      author='Marc Brinkmann',
      author_email='git@marcbrinkmann.de',
      url='http://github.com/mbr/',
      packages=['wtfuniform'],
      package_data = {'wtfuniform': ['templates/*']},
      install_requires=['wtforms', 'jinja2>=2.4'],
     )
