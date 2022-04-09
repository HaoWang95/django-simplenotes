import string
from django import forms
from django.core.exceptions import ValidationError

from .models import Note
"""
Using Django forms to handle form validation
"""
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-5'}),
            'text': forms.TextInput(attrs={'class':'form-control my-5'})
        }
        labels = {
            'text': 'Write your thoughts and comments'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('Note should be about Django!')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 10:
            raise ValidationError('You need to make a note properly!')
        return text