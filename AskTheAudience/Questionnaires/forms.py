from django import forms
from Questionnaires.models import Question

class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text' : forms.TextInput(
                attrs={ 'class' : "form-control", 'placeholder' : "Give me a text..." }
            )
        }
