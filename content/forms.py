from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.BsitEmail
        fields = ['fullname', 'email']

        widgets = {
            'fullname' : forms.TextInput(attrs={
                "placeholder":"e.g Lastname, Firstname M.I",
                "minlength":"4",
                "class":"form-control btn-block",
                "autocomplete":"off",
            }),
            'email' : forms.TextInput(attrs={
                "data-rule":"required",
                "minlength":"4",
                "class":"form-control ",
                "placeholder": "e.g myusername@gmail.com",
                "autocomplete":"off",

            })
        }