# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from .models import *


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean_text(self):
        text = self.cleaned_data['text']
        # if not is_ethic(message):
        #     raise forms.ValidationError(
        #         u'Сообщение не корректно', code=12)
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']  # , 'content', 'category', 'tags']

    # def __init__(self, *args, **kwargs):
    #     super(AnswerForm, self).__init__(*args, **kwargs)
    #     # self.fields['question_id'].initial = "24"
    #     # self.cleaned_data['question'] = '24'

    def save(self, id):     # ???????????????
        self.cleaned_data['question_id'] = id
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
