from django import forms
from django.forms import formset_factory

from .models import Question, Answer, Test


class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ('name', )


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('name', )


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('name', 'key', )


formset_answer = formset_factory(
    AnswerForm, extra=2, max_num=2, min_num=2, validate_min=True, validate_max=True)
