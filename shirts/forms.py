from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, label='Name',)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')