from django.shortcuts import render
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def new_topic(request):
    """Adiciona um novo assunto"""
    if request.method != 'POST':
        # Nenhuma dado submetido; cria um formulario em branco
        form = TopicForm()
    else:
        # Dados de POST submetido; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
        
        context = {'form': form}
        return render(request, 'LearningLogs/new_topic.html', context)