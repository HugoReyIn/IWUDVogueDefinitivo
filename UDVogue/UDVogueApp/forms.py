from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'mail_text', 'placeholder': 'Nombre'})
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'class': 'mail_text', 'placeholder': 'Correo electrónico'})
    )
    phone = forms.CharField(
        label="Número de teléfono", 
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'mail_text', 'placeholder': 'Número de teléfono'})
    )
    comments = forms.CharField(
        label="Comentarios",
        widget=forms.Textarea(attrs={'class': 'massage-bt', 'placeholder': 'Comentarios', 'rows': 5})
    )
