from django.views import View
from django.http import JsonResponse, QueryDict
from django.views.generic import DetailView

from polls.models import Question, Answer, Poll
from django.core import serializers


class QuestionList(View):
    def get(self, request):
        # serialized_response = serializers.serialize('json', Question.objects.all())
        questions = Question.objects.values('id', 'question_text')
        question_list = list(questions)
        return JsonResponse({"questions": question_list})

    def delete(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return JsonResponse(
                {"error": f"Question with id {pk} does not exist!"}, status=404)
        question.delete()
        return JsonResponse({})


class QuestionDetail(View):
    def get(self, request, pk):

        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return JsonResponse(
                {"error": f"Question with id {pk} does not exist!"}, status=404)
        return JsonResponse(
            {
                "id": question.id,
                "question_text": question.question_text,
                "pub_date": question.pub_date
            }
        )

    def put(self, request, pk):
        body = QueryDict(request.body)
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return JsonResponse(
                {"error": f"Question with id {pk} does not exist!"},
                status=404
            )
        question.question_text = body["question_text"]
        question.save(update_fields=["question_text"])
        return JsonResponse(
            {
                "id": question.id,
                "question_text": question.question_text,
                "pub_date": question.pub_date
            }
        )


# GET

class AnswerList(View):
    def get(self, request):
        answers = Answer.objects.values('id', 'answer_text')
        answers_list = list(answers)
        return JsonResponse({"answers": answers_list})


class AnswerDetail(View):
    def get(self, request, pk):
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            return JsonResponse(
                {"error": f"Answer with id {pk} does not exist!"}, status=404)
        return JsonResponse(
            {
                "id": answer.id,
                "answer_text": answer.answer_text,
                "date_added": answer.date_added
            }
        )


class PollList(View):
    def get(self, request):
        polls = Poll.objects.values('id', 'name')
        polls_list = list(polls)
        return JsonResponse({"polls": polls_list})
