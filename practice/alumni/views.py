from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import AlumniForm

def createAlumni(request):
    if request.method == "POST":
        form = AlumniForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
    else:
        form = AlumniForm()
    return render(request, 'form.html', {'form': form})