```python
from wtfuniform import TextField, PasswordField, SubmitField, Form, validators

class LoginForm(Form):
	username = TextField('Your username', [validators.Required()])
	password = PasswordField('Your password', [validators.Required()])
	login = SubmitField('Login')
```
