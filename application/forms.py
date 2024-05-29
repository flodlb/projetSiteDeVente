from django import forms
from django.urls import reverse_lazy
from django.views import generic

from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
            'pub_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),

        }
        labels = {
            'question_text': 'pub_date',
            'pub_date': 'Date de publication',
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']
        widgets = {
            'choice_text': forms.TextInput(attrs={'class': 'form-control'}),
            'pub_date': forms.NumberInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),

        }
        labels = {
            'question': 'Question',
            'choice_text': 'Choix:',
            'votes': 'Votes:',
        }
        
