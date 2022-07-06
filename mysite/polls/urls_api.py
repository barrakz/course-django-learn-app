from django.urls import path
from polls import views_api

app_name = "polls_api"

urlpatterns = [
    path("questions/", views_api.QuestionList.as_view(), name="questions"),
    path("questions/<pk>", views_api.QuestionDetail.as_view(), name="questions-detail"),

    path("answers/", views_api.AnswerList.as_view(), name="answers"),
    path("answers/<pk>", views_api.AnswerDetail.as_view(), name="answers"),

    path("polls/", views_api.PollList.as_view(), name="polls"),


]

