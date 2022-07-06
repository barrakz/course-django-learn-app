from django.urls import path

from . import views

app_name = "polls_view"


urlpatterns = [
    path("hello/<s0>/", views.hello, name="hello"),
    path('hello-year/', views.hello_year),
    path('my-animals/', views.animals),
    path("index/", views.index, name="index"),
    path("polls/", views.polls, name="polls"),
    path("answers/", views.answers, name="answers"),
    path("questions/", views.questions, name="questions"),
    path("name-form/", views.get_name, name="name-form"),
    path("poll-form/", views.poll_form, name="poll-form"),
    path("question-form/", views.question_form, name="question-form"),
    path("answer-form/", views.answer_form, name="answer-form"),

]
