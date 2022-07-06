from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import AnswerForm, NameForm, PollForm, QuestionForm
from .models import Answer, Poll, Question


def capitalize_check(user):
    if user.username:
        return user.username[0].isupper()
    return False


def first_letter_a(user):
    if user.username:
        return user.username[0] == "a"
    return False


def hello(request, s0):
    s1 = request.GET.get("s1", "")
    return render(
        request,
        template_name="polls/hello.html",
        context={"adjectives": [s0, s1, "beautiful", "horrible", "nice"]}
    )


def hello_year(request):
    year = request.GET.get("year", "No key in the dictionary!")
    return HttpResponse(f"Optional argument: {year}")
    # return HttpResponseRedirect(reverse("polls:answers-list-view"))


def animals(request):
    animals_list = request.GET.get("animals", "").split(",")
    return render(
        request,
        template_name="polls/my_template.html",
        context={"animals": animals_list}
    )


@user_passes_test(capitalize_check)
def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse("IT WORKED!")
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )
    return render(
        request,
        template_name="form.html",
        context={"form": NameForm()}
    )


def index(request):
    return render(
        request,
        template_name="polls/index.html"
    )


@permission_required("polls.view_poll", raise_exception=True)
@login_required
def polls(request):
    print(request.user.is_authenticated)
    return render(
        request,
        template_name="polls/polls.html",
        context={"polls": Poll.objects.all()}
    )


def answers(request):
    return render(
        request,
        template_name="polls/answers.html",
        context={"answers": Answer.objects.all()}
    )


def questions(request):
    return render(
        request,
        template_name="polls/questions.html",
        context={"questions": Question.objects.all()}
    )


def poll_form(request):
    form = PollForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data["name"]
        Poll.objects.create(name=name)
        return render(
            request,
            template_name="polls/polls.html",
            context={"polls": Poll.objects.all()}
        )
    return render(
        request,
        template_name="polls/form.html",
        context={"form": form}
    )


@user_passes_test(first_letter_a)
def question_form(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question_text = form.cleaned_data["question_text"]
        poll = form.cleaned_data["poll"]
        Question.objects.create(question_text=question_text, poll=poll)
        return HttpResponse("IT WORKED")
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )


def answer_form(request):
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        answer_text = form.cleaned_data["answer_text"]
        Answer.objects.create(answer_text=answer_text)
        return HttpResponse("IT WORKED")
    return render(
        request,
        template_name="polls/form.html",
        context={"form": form}
    )
