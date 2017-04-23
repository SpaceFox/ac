from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder
from crispy_forms.bootstrap import StrictButton

from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(
        label='Votre nom',
        max_length=200,
        required=True,
    )
    email = forms.EmailField(
        label='Votre adresse courriel',
        required=True,
    )
    subject = forms.CharField(
        label='Sujet',
        max_length=200,
        required=True,
    )
    message = forms.CharField(
        label='Votre message',
        required=True,
        widget=forms.Textarea(),
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-alone'
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('name'),
            Field('email'),
            Field('subject'),
            Field('message'),
            ButtonHolder(
                StrictButton('Envoyer', type='submit'),
            )
        )