from django.contrib import admin

from .models import Question, Test, Answer, Respondent_Answer, CustomUser
# Register your models here.


@admin.register(CustomUser)
class CustomUserOptions(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionOptions(admin.ModelAdmin):
    pass


@admin.register(Test)
class TestOptions(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerOptions(admin.ModelAdmin):
    pass


@admin.register(Respondent_Answer)
class Respondent_AnswerOptions(admin.ModelAdmin):
    pass
