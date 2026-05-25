from django import forms
from django.forms import inlineformset_factory
from polls.models import Question, Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'publisher']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Frage eingeben'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Veröffentlicher'}),
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        widgets = {
            'choice_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Antwortmöglichkeit'}),
        }


# Formset für mehrere Choices
ChoiceFormSet = inlineformset_factory(
    Question,
    Choice,
    form=ChoiceForm,
    extra=3,  # 3 zusätzliche leere Forms
    can_delete=False
)

