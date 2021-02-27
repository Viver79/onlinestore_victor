from django import forms
from .models import UserMessages


class UserMessagesForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'type':'text', 'placeholder':"NAME", 'required':''}))
    surname = forms.CharField(max_length=50,
                              widget=forms.TextInput(attrs={'type':'text', 'placeholder':"SURNAME", 'required':''}))
    user_email = forms.EmailField(widget=forms.TextInput(attrs={'class':"user", 'type':"text",
                                                                'placeholder':"USER@DOMAIN.COM", 'required':""}))
    message = forms.CharField(max_length=200,
                              widget=forms.Textarea(attrs={'placeholder':"MESSAGE"}))

    class Meta():
        model = UserMessages
        fields = ('name', 'surname', 'user_email', 'message')
