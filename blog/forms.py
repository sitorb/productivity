from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

        widget = {
            "text": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Comment"
            })
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            "title",
            "description",
            "photo",
            "category"
        )
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control"
            }),
            "photo": forms.FileInput(attrs={
                "class": "form-control"
            }),
            "category": forms.Select(attrs={
                "class": "form-select"
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Name", max_length=150,
                               widget=forms.TextInput(attrs={
                                   "class": "form-control mb-3"
                               }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "class": "form-control"
    }))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Name", max_length=150,
                               widget=forms.TextInput(attrs={
                                   "class": "form-control mb-3",
                                   "placeholder": "Name"
                               }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control mb-3",
        "placeholder": "Password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control mb-3",
        "placeholder": "Confirm password"
    }))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
