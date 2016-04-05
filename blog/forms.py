from django import  forms

class  LoginForm(forms.Form):
    email = forms.EmailField()
    passwd = forms.CharField(widget=forms.PasswordInput)
class RegisterForm(forms.Form):
    email = forms.EmailField()
    nickname = forms.CharField()
    passwd = forms.CharField(widget=forms.PasswordInput)
    passwd2 = forms.CharField(widget= forms.PasswordInput)
    job = forms.CharField()
    address = forms.CharField()
    label = forms.CharField()
    birthday = forms.DateField(widget=forms.SelectDateWidget)
