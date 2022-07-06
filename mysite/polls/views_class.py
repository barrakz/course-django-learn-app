from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import FormView, ListView, TemplateView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse

from .forms import (
    AnswerForm,
    AnswerModelForm,
    PollForm,
    PollModelForm,
    QuestionForm,
    QuestionModelForm
)

from .models import Poll, Question, Answer


class UsernameCheckMixin(UserPassesTestMixin):

    def test_func(self):
        if self.request.user.username:
            return self.request.user.username[-1].islower()
        return False


class PollView(UsernameCheckMixin, View):
    def get(self, request):
        return render(
            request,
            template_name="polls/polls.html",
            context={"polls": Poll.objects.all()}
        )


class PollTemplateView(TemplateView):
    template_name = "polls/polls.html"
    extra_context = {"polls": Poll.objects.all()}


class PollFormView(FormView):
    template_name = "form.html"
    form_class = PollForm
    success_url = reverse_lazy("polls:polls-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        name = form.cleaned_data["name"]
        Poll.objects.create(name=name)
        return result


class PollModelFormView(FormView):
    template_name = "form.html"
    form_class = PollModelForm
    success_url = reverse_lazy("polls:polls-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result


class PollListView(ListView):
    template_name = "polls/list_view.html"
    model = Poll


class QuestionView(View):
    def get(self, request):
        return render(
            request,
            template_name="polls/questions.html",
            context={"questions": Question.objects.all()}
        )

    def post(self, request):
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            question_text = form.cleaned_data["question_text"]
            poll = form.cleaned_data["poll"]
            Question.objects.create(question_text=question_text, poll=poll)
            return HttpResponseRedirect(reverse("polls:questions-list-view"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )


class QuestionTemplateView(TemplateView):
    template_name = "polls/questions.html"
    extra_context = {"questions": Question.objects.all()}


class QuestionFormView(FormView):
    template_name = "form.html"
    form_class = QuestionForm
    success_url = reverse_lazy("polls:questions-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        question_text = form.cleaned_data["question_text"]
        poll = form.cleaned_data["poll"]
        Question.objects.create(question_text=question_text, poll=poll)
        return result


class QuestionModelFormView(FormView):
    template_name = "form.html"
    form_class = QuestionModelForm
    success_url = reverse_lazy("polls:questions-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result


class QuestionListView(ListView):
    template_name = "polls/list_view.html"
    model = Question


class AnswerView(View):
    def get(self, request):
        return render(
            request,
            template_name="polls/answers.html",
            context={"answers": Answer.objects.all()}
        )


class AnswerTemplateView(TemplateView):
    template_name = "polls/answers.html"
    extra_context = {"answers": Answer.objects.all()}


class AnswerFormView(FormView):
    template_name = "form.html"
    form_class = AnswerForm
    success_url = reverse_lazy("polls:answers-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        answer_text = form.cleaned_data["answer_text"]
        question = form.cleaned_data["question"]
        Answer.objects.create(answer_text=answer_text, question=question)
        return result


class AnswerModelFormView(FormView):
    template_name = "form.html"
    form_class = AnswerModelForm
    success_url = reverse_lazy("polls:answers-list-view")

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result


class AnswerListView(ListView):
    template_name = "polls/list_view.html"
    model = Answer


class QuestionCreateView(CreateView):
    model = Question
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("polls:questions-list-view")


# class QuestionDetailView(View):
#     def get(self, request, pk):
#         return render(
#             request,
#             template_name="questions_form.html",
#             context={"question": get_object_or_404(Question, pk=pk)}
#         )
#

class QuestionUpdateView(View):
    def get(self, request, pk):
        return render(
            request,
            template_name="form.html",
            context={"form": QuestionForm()}
        )

    def post(self, request, pk):
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            q = get_object_or_404(Question, pk=pk)
            q.question_text = form.cleaned_data["question_text"]
            q.poll = form.cleaned_data["poll"]
            q.save()
            return HttpResponseRedirect(reverse("polls:questions-list-view"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

    def post(self, request, pk):
        Question.objects.get(pk=pk).delete()
        return HttpResponseRedirect(reverse("polls:questions-list-view"))


class AnswerCreateView(CreateView):
    model = Answer
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("polls:answers-list-view")


class AnswerUpdateView(View):
    def get(self, request, pk):
        form = AnswerForm()
        return render(
            request,
            template_name="form.html",
            context={"form": AnswerForm()}
        )

    def post(self, request, pk):
        form = AnswerForm(request.POST or None)
        if form.is_valid():
            q = get_object_or_404(Answer, pk=pk)
            q.answer_text = form.cleaned_data["answer_text"]
            q.poll = form.cleaned_data["poll"]
            q.save()
            return HttpResponseRedirect(reverse("polls:answers-list-view"))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )


class QuestionDetailView(View):
    def get(self, request, pk):
        return render(
            request,
            template_name="polls/my_question.html",
            context={"question": get_object_or_404(Question, pk=pk)}
        )


class AnswerDetailView(View):
    def get(self, request, pk):
        return render(
            request,
            template_name="polls/my_answer.html",
            context={"answer": Answer.objects.get(pk=pk)}
        )


class QuestionDetailClassView(DetailView):
    model = Question
    template_name = "polls/my_question.html"


class QuestionUpdateGenericView(UpdateView):
    model = Question
    fields = ("question_text",)
    template_name = "form.html"
    success_url = reverse_lazy("polls:questions-list-view")


class QuestionDeleteView(View):
    def get(self, request, pk):
        return render(
            request,
            template_name="polls/delete.html",
            context={"object": get_object_or_404(Question, pk=pk)}
        )

    def post(self, request, pk):
        Question.objects.get(pk=pk).delete()
        return HttpResponseRedirect(reverse("polls:questions-list-view"))


class QuestionDeleteGenericView(DeleteView):
    model = Question
    template_name = "polls/delete.html"
    success_url = reverse_lazy("polls:questions-list-view")


class PollDetailView(DetailView):

    model = Poll
    template_name = "polls/my_poll.html"


class PollUpdateView(UpdateView):
    model = Poll
    fields = ("name",)
    template_name = "form.html"
    success_url = reverse_lazy("polls:polls-list-view")


class PollDeleteView(DeleteView):
    model = Poll
    template_name = "polls/delete.html"
    success_url = reverse_lazy("polls:poll-list-view")
