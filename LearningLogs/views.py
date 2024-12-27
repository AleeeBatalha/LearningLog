from django.shortcuts import render
from .models import Topic

def index(request):
    """Pagina principal do LearningLog"""
    return render(request, 'LearningLogs/index.html')

def topics(request):
    """Mostra a todos os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'LearningLogs/topics.html', context)

def topic(request, topic_id):
    """Mostra um unico assunto e todas as suas entradas."""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'LearningLogs/topic.html', context)