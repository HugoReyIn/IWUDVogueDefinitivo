from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre", widget=forms.TextInput(attrs={
        'class': 'mail_text', 'placeholder': 'Nombre'
    }))
    correo = forms.EmailField(label="Correo Electrónico", widget=forms.TextInput(attrs={
        'class': 'mail_text', 'placeholder': 'Correo electrónico'
    }))
    telefono = forms.CharField(max_length=15, label="Número de Teléfono", widget=forms.TextInput(attrs={
        'class': 'mail_text', 'placeholder': 'Número de teléfono'
    }))
    comentarios = forms.CharField(label="Comentarios", widget=forms.Textarea(attrs={
        'class': 'massage-bt', 'placeholder': 'Comentarios', 'rows': 5
    }))
