from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, ListView, FormView, CreateView

from .models import Test, Question, Answer, Respondent_Answer, CustomUser
from .forms import QuestionForm, TestForm, formset_answer
from .resultst_test import test_1


class TestDetailView(DetailView):
    model = Test
    fields = '__all__'
    template_name = 'platform/test_detail.html'
    context_object_name = "test"


class TestCreateView(CreateView):
    model = Test
    fields = ['name', ]
    template_name = 'platform/add_test.html'


class AddQuestionView(View):
    def get(self, request, *args, **kwargs):
        test = Test.objects.get(id=kwargs['pk'])
        form = QuestionForm()
        return render(request, 'platform/add_question.html', context={'test': test, 'form': form})

    def post(self, request, *args, **kwargs):
        test = Test.objects.get(id=kwargs['pk'])
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.instance.test = test
            question = form.save()
            return redirect(question)


class AddAnswerView(View):
    def get(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs['pk_q'])
        form = formset_answer()
        return render(request, 'platform/add_question.html', context={'question': question, 'form': form})

    def post(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs['pk_q'])
        form = formset_answer(request.POST)
        if form.is_valid():
            for i in form.cleaned_data:
                Answer.objects.create(
                    question=question, name=i['name'], key=i['key'])

            return redirect(question.test.get_absolute_url())


class TestList(ListView):
    model = Test

    template_name = 'platform/test_list.html'
    context_object_name = 'tests'


class RunTest(View):
    def get(self, request, *args, **kwargs):
        test = Test.objects.get(id=kwargs['pk'])
        return render(request, 'platform/test_run.html', context={'test': test})

    def post(self, request, *args, **kwargs):
        test = Test.objects.get(id=kwargs['pk'])
        list_id_q = test.questions.values_list('pk', flat=True)
        for id_q in list_id_q:
            question = Question.objects.get(id=id_q)
            answer_key = Answer.objects.get(
                name=request.POST[str(id_q)]).key
            answer_respondent = Respondent_Answer.objects.create(
                respondent=request.user, question=question, key=answer_key, name=request.POST[str(id_q)])
        test.respondents.add(request.user)

        return render(request, 'platform/test_run.html', context={'test': test})


class StartTest(View):
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        if user.soul == '':
            test = Test.objects.get(name='ABC')
            return render(request, 'platform/test_run.html', context={'test': test})
        return render(request, 'respondent/profile.html')

    def post(self, request, *args, **kwargs):
        test = Test.objects.get(name='ABC')
        list_id_q = test.questions.values_list('pk', flat=True)
        key_soul = ''
        for id_q in list_id_q:
            question = Question.objects.get(id=id_q)
            print(question)
            print(request.POST)
            answer_key = Answer.objects.get(
                name=request.POST[str(id_q)]).key
            answer_respondent = Respondent_Answer.objects.create(
                respondent=request.user, question=question, key=answer_key, name=request.POST[str(id_q)])
            key_soul += answer_key

        print(key_soul)
        user = CustomUser.objects.get(id=request.user.id)
        user.soul_key = key_soul
        soul = test_1[key_soul]
        print(soul)
        user.soul = soul[0]
        user.save()
        test.respondents.add(user)

        return render(request, 'platform/test_run.html', context={'user': user, 'test': test})
