from .models import user_profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class SignupForm(UserCreationForm):
    email = forms.EmailField()    # custom field for sign up form

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

        labels = {'password1':'Password','password2':'Confirm Password'}


# user - teacher can only be  created by admin so here no teacher in profile creation form so no one can create profile as teacher
class ProfileForm(ModelForm):

    bio = forms.CharField(required=False)
    user_types = [('parent','parent'),('student','student')]
    user_type = forms.ChoiceField(required=True, choices=user_types)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = user_profile
        fields = ['bio', 'profile_pic', 'user_type']
        # no user field above because we will directly get user field from login user, see in view.py