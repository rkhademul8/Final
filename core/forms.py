from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class SignUpForm(UserCreationForm):
	class Meta:
		model=CustomUser
		fields=('email','first_name','last_name','phone','profile_image')