# Django Users Boilerplate

[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=102)](https://github.com/vigzmv/Django-Users-boilerplate)  &nbsp;&nbsp;
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/vigzmv/Django-Users-boilerplate)  &nbsp;&nbsp;
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/vigzmv/Django-Users-boilerplate)

### A Django boilerplate with User Registeration, Login and Password change views.    
This boilerplate can be used to create Django projects with user management quicker.
  
## Usage

  ```sh
  # Get project locally
  $ git clone https://github.com/vigzmv/Django-Users-boilerplate.git
  
  # Rename directory
  $ mv Django-Users-boilerplate **Your_project_dir_name**
  $ cd **Your_project_dir_name**
  
  # Install requirements
  $ pip install -r requirements.txt
  
  # Runserver
  $ python manage.py runserver
  
  # Done! Make required changes in 'App' as required to create your Django App.
  ```
  
<br>

## Customisation

### User registration fields
The fields of User object can be changed by editing the required 'fields' in App/forms.py.
```py
class UserSignUpForm(forms.ModelForm):
 class Meta:
  model = User
    
  # change fields of User Object here
  fields = ('username','password','email','first_name','last_name',)
  
  help_texts = {
   'username': None,
   }
  widgets = {
  'password':forms.PasswordInput(),
  }
```

Refer Docs: https://docs.djangoproject.com/en/1.10/ref/contrib/auth/

## Also included
* bootstrap-v3.3.6-min.css
* bootstrap-v3.3.6-min.js
* jquery-v2.2.0.min.js
