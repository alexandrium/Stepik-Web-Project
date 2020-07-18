# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import AuthenticationForm, password_validation, UsernameField


# class UserCreationForm(forms.Form):
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password")
#         field_classes = {'username': UsernameField}
#
#     # def _post_clean(self):
#     #     super()._post_clean()
#     #     # Validate the password after self.instance is updated with form data
#     #     # by super().
#     #     password = self.cleaned_data.get('password')
#     #     if password:
#     #         try:
#     #             password_validation.validate_password(password)
#     #         except forms.ValidationError as error:
#     #             self.add_error('password', error)
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'autofocus': True}))
    # username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def _post_clean(self):
        # super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password')
        if password:
            try:
                password_validation.validate_password(password)
            except forms.ValidationError as error:
                self.add_error('password', error)

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     if password:
    #         try:
    #             password_validation.validate_password(password)
    #         except forms.ValidationError as error:
    #             self.add_error('password', error)

    def save(self):
        from django.contrib.auth.models import User
        # user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password'])

        # user = User(**self.cleaned_data)
        user = User()
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])

        user.save()
        return user
                    # # # #


class AskForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'autofocus': True}))
    text = forms.CharField(widget=forms.Textarea, required=False)

    def clean_text(self):
        text = self.cleaned_data['text']
        # if not is_ethic(message):
        #     raise forms.ValidationError(
        #         u'Сообщение не корректно', code=12)
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        if hasattr(self, '_user'):
            # if self._user is User():
            question.author = self._user
        question.save()
        return question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
        # fields = ['text', 'question']  # , 'content', 'category', 'tags']

    # def __init__(self, *args, **kwargs):
    #     super(AnswerForm, self).__init__(*args, **kwargs)
    #     # self.fields['question'].initial = "24"
    #     # # self.cleaned_data['question'] = '24'

    def save(self, id):     # ???????????????
        # self.cleaned_data['question_id'] = id
        answer = Answer(**self.cleaned_data)
        answer.question_id = id
        if hasattr(self, '_user'):
            answer.author = self._user
        answer.save()
        return answer
        # return
