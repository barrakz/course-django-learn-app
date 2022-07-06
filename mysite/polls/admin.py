from django.contrib import admin

from polls.models import Answer, Poll, Question


class QuestionAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'question_text', 'pub_year')
    list_display_links = ('id', 'question_text')
    list_per_page = 10
    list_filter = ('pub_date',)
    search_fields = ('question_text',)
    actions = ('cleanup_text',)

    fieldsets = [
        ("General", {
            "fields": ["id", "question_text"],
            "description": "General info"
        }),

        ("External information", {
            "fields": ["pub_date", "poll"],
            "description": "External Info"
        })

    ]
    readonly_fields = ["pub_date", "id"]

    @staticmethod
    def pub_year(obj):
        return obj.pub_date.year

    @staticmethod
    def cleanup_text(modeladmin, request, queryset):
        queryset.update(question_text="")


class AnswerAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'answer_text', 'pub_month')
    list_display_links = ('id', 'answer_text',)
    list_per_page = 10
    list_filter = ('date_added',)
    search_fields = ('answer_text',)
    actions = ('add_suffix',)

    fieldsets = [
        ("General", {
            "fields": ["id", "answer_text"],
            "description": "General info"
        }),

        ("External information", {
            "fields": ["date_added", "question"],
            "description": "External Info"
        })

    ]
    readonly_fields = ["date_added", "id"]

    @staticmethod
    def pub_month(obj):
        return obj.date_added.month

    @staticmethod
    def add_suffix(modeladmin, request, queryset):
        for obj in queryset:
            obj.answer_text += "-example"
        Answer.objects.bulk_update(queryset, ["answer_text"])


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Poll)
admin.site.register(Question, QuestionAdmin)
