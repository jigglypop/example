from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth import get_user_model

class CustromUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()    # User
        fields = ('username','first_name','last_name',)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','first_name','last_name','email')
        
    