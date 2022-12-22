from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

#class Emp(forms.ModelForm):
    #class Meta:
        #model=Employe
        #fields=['username','fname','lname']
class Registrf(UserCreationForm):
      class Meta:
          model=User
          fields=['username','email','password1','password2','type']
      def __init__(self, *args, **kwargs):
        super(Registrf, self).__init__(*args, **kwargs)
        self.fields['username'].label = "enter username"
        self.fields['password1'].label = "new password"
        self.fields['type'].label = "choose type of new user"
        #self.fields['username'].widget.attrs['class'] = 'form-control'

        
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'
          

