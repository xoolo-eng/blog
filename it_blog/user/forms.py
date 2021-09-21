from django import forms


class UserSignIn(forms.Form):
    username = forms.CharField(
        label="User name",
        widget=forms.TextInput(
            attrs={
                "id": "name",
                "class": "form-control",
                "placeholder": "User name",
                "onfocus": "this.placeholder = ''",
                "onblur": "this.placeholder = 'User name'"
            }
        ),
    )
    phone = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField()
    repeat_password = forms.CharField()
    is_agree = forms.BooleanField()
