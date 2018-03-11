from django import forms
from qa.models import Question, Answer
from datetime import datetime

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    
    def clean__title(self):
        if not len(title):
            raise forms.ValidationError('Wrong title', code='spam' )
    def clean__text(self):
        if not len(text):
            raise forms.ValidationError('Wrong text', code='spam' )

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question_id = forms.IntegerField(widget=forms.HiddenInput)
    
    def clean__text(self):
        if not len(text):
            raise forms.ValidationError('Wrong text', code='spam' )

    def save(self, question_id):
        qu = Question.objects.get(pk = question_id)
        answer = Answer(**self.cleaned_data)
        answer.question = qu
        answer.save()
