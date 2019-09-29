from django.urls import path

from .views import (TestDetailView, AddQuestionView,
                    AddAnswerView, TestList, RunTest,
                    TestCreateView, StartTest)

urlpatterns = [
    path('', TestList.as_view(), name='test_list'),
    path('add/', TestCreateView.as_view(), name='test_add'),
    path('start_test/', StartTest.as_view(), name='start_test'),
    path('<str:pk>/run/', RunTest.as_view(), name='test_run'),
    path('<str:pk>/', TestDetailView.as_view(), name='detail_test'),
    path('<str:pk>/add_q', AddQuestionView.as_view(), name='add_q'),
    path('<str:pk>/add_q/<str:pk_q>/', AddAnswerView.as_view(), name='add_a'),

]
