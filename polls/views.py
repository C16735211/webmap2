from django.shortcuts import render
from .models import Question, Choice


# Question - Display
def index(request):
    return render(request, 'polls/templates/polls/index.html')
