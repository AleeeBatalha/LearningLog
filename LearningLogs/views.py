from django.shortcuts import render
from .models import Topic

def index(request):
    """Pagina principal do LearningLog"""
    return render(request, 'LearningLogs/index.html')

def topics(request):
    """Mostra a todos os assuntos"""
    topic = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'LearningLogs/topics.html', context)