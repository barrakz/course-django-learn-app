from django.urls import path

from . import views_class

app_name = "polls"

urlpatterns = [
    path("polls-class-view/", views_class.PollView.as_view(), name="polls-class-view"),
    path(
        "polls-template-view/", views_class.PollTemplateView.as_view(), name="polls-template-view"
    ),
    path("polls-list-view/", views_class.PollListView.as_view(), name="polls-list-view"),
    path("polls-form-view/", views_class.PollFormView.as_view(), name="polls-form-view"),
    path(
        "polls-model-form-view/",
        views_class.PollModelFormView.as_view(),
        name="polls-model-form-view"
    ),
    path("questions-class-view/", views_class.QuestionView.as_view(), name="questions-class-view"),
    path(
        "questions-template-view/",
        views_class.QuestionTemplateView.as_view(),
        name="questions-template-view"
    ),
    path(
        "questions-list-view/", views_class.QuestionListView.as_view(), name="questions-list-view"
    ),
    path(
        "questions-form-view/", views_class.QuestionFormView.as_view(), name="questions-form-view"
    ),
    path(
        "questions-model-form-view/",
        views_class.QuestionModelFormView.as_view(),
        name="questions-model-form-view"
    ),
    path("answers-class-view/", views_class.AnswerView.as_view(), name="answers-class-view"),
    path(
        "answers-template-view/",
        views_class.AnswerTemplateView.as_view(),
        name="answers-template-view"
    ),
    path("answers-list-view/", views_class.AnswerListView.as_view(), name="answers-list-view"),
    path("answers-form-view/", views_class.AnswerFormView.as_view(), name="answers-form-view"),
    path(
        "answers-model-form-view/",
        views_class.AnswerModelFormView.as_view(),
        name="answers-model-form-view",
    ),
    path("question-create-view/", views_class.QuestionCreateView.as_view(), name="question-create-view"),
    path("question-update-view/<pk>/", views_class.QuestionUpdateView.as_view(), name="question-update-view"),
    path(
        "question-update-generic-view/<pk>",
        views_class.QuestionUpdateGenericView.as_view(),
        name="question-update-generic-view"),

    path("answer-create-view/", views_class.AnswerCreateView.as_view(), name="answer-create-view"),
    path("answer-update-view/<pk>", views_class.AnswerUpdateView.as_view(), name="answer-update-view"),
    path("questions-detail-view/<pk>/", views_class.QuestionDetailView.as_view(), name="question-detail-view"),
    path("answers-detail-view/<pk>/", views_class.AnswerDetailView.as_view(), name="answer-detail-view"),
    path("questions-detail-class-view/<pk>/", views_class.QuestionDetailClassView.as_view(), name="answer-detail-view"),
    path("questions-delete-view/<pk>", views_class.QuestionDeleteView.as_view(), name="question-delete-view"),
    path(
        "questions-delete-generic-view/<pk>",
        views_class.QuestionDeleteGenericView.as_view(),
        name="question-delete-generic-view"
    ),
    path("polls-detail-view/<pk>", views_class.PollDetailView.as_view(), name="polls-detail-view"),
    path("polls-update-view/<pk>", views_class.PollUpdateView.as_view(), name="polls-update-view"),
    path("polls-delete-view/<pk>", views_class.PollDeleteView.as_view(), name="polls-delete-view"),

]
