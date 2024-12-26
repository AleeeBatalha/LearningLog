from django.shortcuts import render

def index(request):
    """Pagina principal do LearningLog"""
    return render(request, 'LearningLogs/index.html')
