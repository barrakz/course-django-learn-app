from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    question_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name="questions", blank=True, null=True
    )

    def __str__(self):
        return f"{self.question_text}"


class Answer(models.Model):
    answer_text = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers", blank=True, null=True
    )

    def __str__(self):
        return f"{self.answer_text}"
