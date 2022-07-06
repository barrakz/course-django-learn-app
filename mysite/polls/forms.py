from datetime import datetime
import pytz

from django import forms
from django.core.exceptions import ValidationError

from polls.models import Answer, Poll, Question

utc = pytz.UTC


class PastDateTimeField(forms.DateTimeField):
    def validate(self, value):
        super().validate(value)
        if value >= datetime.today().replace(tzinfo=utc):
            raise ValidationError("Date must be in the past.")


class LowerLetterField(forms.CharField):
    def validate(self, value):
        super().validate(value)
        if value[0].isupper():
            raise ValidationError("Value must start with lower letter.")


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Value must be capitalized.")


def upper_letter_validator(value):
    if value.isupper():
        raise ValidationError("Value cannot be written in uppercase.")


class NameForm(forms.Form):
    name = forms.CharField(max_length=128)
    birth_date = forms.DateField()


class PollForm(forms.Form):
    name = LowerLetterField(max_length=128)

    # def clean_name(self):
    #     return self.cleaned_data["name"].upper()


class PollModelForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = "__all__"


class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=128, validators=[])
    # pub_date = PastDateTimeField(label="Publication Date")
    poll = forms.ModelChoiceField(queryset=Poll.objects.all())

    # def clean_question_text(self):
    #     return self.cleaned_data["question_text"].lower()

    def clean(self):
        result = super().clean()
        if not self.errors:
            if result["question_text"][0] == "A" and result["pub_date"].year < 2000:
                self.add_error("question_text", "Don't start with an A")
                self.add_error("pub_date", "Year must be after 1999")
                raise ValidationError("Can't start with an A and year before 2000")
            if result["question_text"][0] == "w" and result["pub_date"] < datetime.now().replace(tzinfo=utc):
                self.add_error("question_text", "Don't start with a w")
                self.add_error("pub_date", "Date must be in the future")
                raise ValidationError("Can't start with a w and date from past")
        return result


class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerForm(forms.Form):
    answer_text = forms.CharField(max_length=128, validators=[upper_letter_validator])
    question = forms.ModelChoiceField(queryset=Question.objects.all())


class AnswerModelForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"
