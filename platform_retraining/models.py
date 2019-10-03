from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    soul_key = models.CharField(
        max_length=4, verbose_name='ключ от души', blank=True)
    soul = models.CharField(
        max_length=200, verbose_name='Душа)))))))', blank=True)


class Test(models.Model):
    name = models.CharField(
        max_length=200, verbose_name='Тест')
    respondents = models.ManyToManyField(
        CustomUser, blank=True, related_name='tests')

    def get_absolute_url(self):
        return reverse('detail_test', kwargs={'pk': self.pk})


class Question(models.Model):
    test = models.ForeignKey(
        'Test', on_delete=models.CASCADE, related_name='questions')
    name = models.CharField(max_length=200, verbose_name='Вопрос')

    def get_absolute_url(self):
        return reverse('add_a', kwargs={'pk': self.test.pk, 'pk_q': self.pk})


class Answer(models.Model):
    question = models.ForeignKey(
        'Question', on_delete=models.CASCADE, related_name='answers')
    name = models.CharField(max_length=200, verbose_name='ответ')
    key = models.CharField(max_length=1, verbose_name='ответ - key')

    def __str__(self):
        return "answer for question-%s" % self.question.id


class Respondent_Answer(models.Model):
    question = models.ForeignKey(
        'Question', on_delete=models.CASCADE, related_name='rspondent_answers')
    name = models.CharField(max_length=200, verbose_name='ответ')
    key = models.CharField(max_length=1, verbose_name='ответ - key')
    respondent = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='respondent_answers')
