from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CreateForm(UserCreationForm) :
    class Meta :
        model = User
        fields = ["username", "email", "password1", "password2"]
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields["username"].label=''
        self.fields["email"].label=''
        self.fields["password1"].label=''
        self.fields["password2"].label=''
        self.fields["password1"].help_text=None
        self.fields["username"].help_text=None
        self.fields["password2"].help_text=None

        self.fields["username"].widget.attrs.update({"placeholder":"Username","class":"form-control","class":"mb-3" })
        self.fields["email"].widget.attrs.update({"placeholder":"Email","class":"form-control","class":"mb-3"})
        self.fields["password1"].widget.attrs.update({"placeholder":"Password","class":"form-control","class":"mb-3"})
        self.fields["password2"].widget.attrs.update({"placeholder":"Password Confirmation","class":"form-control","class":"mb-3"})
class AuthForm(AuthenticationForm) :
    class Meta :
        model = User
        fields = ["username", "password"]
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields["username"].label=''
        self.fields["password"].label=''
        self.fields["username"].widget.attrs.update({"placeholder":"Username","class":"form-control","class":"mb-3"})
        self.fields["password"].widget.attrs.update({"placeholder":"Password","class":"form-control","class":"mb-3"})