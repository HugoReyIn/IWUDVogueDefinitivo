from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email')
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)