from django.shortcuts import render
from alumni.models import Alumni


def index(request):

    return render(request, 'index.html')
def stories(request):
    alumni_list = Alumni.objects.all()
    return render(request, 'stories.html', {
        'alumni_list':alumni_list,
    })
