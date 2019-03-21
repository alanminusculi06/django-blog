from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .mail import send_mail_template
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class Contact(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome', 'id': 'name', 'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'id': 'email', 'class': 'form-control'}))
    phone = forms.CharField(label='Telefone', widget=forms.TextInput(attrs={'placeholder': 'Telefone', 'id': 'phone', 'class': 'form-control'}))
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'placeholder': 'Mensagem', 'id': 'message', 'class': 'form-control', 'rows': '5'}))

    def send_mail(self):
        subject = 'Contato'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'phone': self.cleaned_data['phone'],
            'message': self.cleaned_data['message']
        }
        template_name = 'email.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])
