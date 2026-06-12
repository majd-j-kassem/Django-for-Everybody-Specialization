from django.contrib import admin
from .models import Question, Answer
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date' )
    
    # Register your models here.

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question','choice_set','choice_poll')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

