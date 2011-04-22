Pretty forms with uni-form and WTForms
======================================
A python module that allows you to use [uni-form](http://sprawsm.com/uni-form/) with [WTForms](http://wtforms.simplecodes.com/) to give you great looking, optionally client-side verified forms very fast.

The `wtfuniform` module extends many of the `wtforms` classes with the needed functionality. Since it imports all the `wtforms` names and has the same structure, you can use it the same way by changing the import.

Example
=======
``` python
# note that the only difference from normal wtforms usage is importing
# from a different module!
from wtfuniform import TextField, PasswordField, SubmitField, Form, validators

class LoginForm(Form):
	username = TextField('Your username', [validators.Required()])
	password = PasswordField('Your password', [validators.Required()])
	login = SubmitField('Login')

# optional, see below: render the form
from wtfuniform.helper import render_form
render_form(LoginForm())
```

The module in detail
====================
To properly work with uni-form, many of the WTForms widgets are extended with extra functionality:

* Widgets have the proper CSS classes (such as `textInput` for text input fields).
* CSS classes for client-side validation are added, uni-form will validate accordingly.
* `BlockLabelsWidget` is a widget that functions almost like a `ListWidget`, but omits the labels. It is used in conjunction with `RadioLabeledInput` and `CheckboxLabeledInput` to produce the proper multi checkbox/radio inputs used in uni-form.
* All of the above is easily accessible by the `CheckMultipleField` for checkboxes. The default `RadioField` is already overriden to use these new widgets.
* The `validators.Email` validator sets a `valid_email` flag. This is required for the widgets to be able to apply the correct CSS classes.
* There is a helper module `wtfuniform.helper` that includes two functions for HTML code generation: `render_field` and `render_form`. For an example on how to use these with [jinja2](http://jinja.pocoo.org), see *formtest.html*.

Extensions
==========
There are some extensions to the code that are not mandated by uni-form. These included:

* `DateField` and `DateTimeField` have extra css classes of `dateInput` and `dateTimeInput`. This makes it easy to attach date selectors using javascript, e.g. by using jQuery.
