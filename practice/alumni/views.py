from django.shortcuts import render, redirect
from .models import *
from .forms import AlumniForm

def alumni_profile(request):
    alumni = Alumni.objects.all()
    return render(request, 'stories.html', {'alumni': alumni})

def alumni(request):
    alumni = Alumni.objects.all()
    return render(request, 'alumni.html', {'alumni': alumni})



def create(request):
    if request.method == 'POST':
        form = AlumniForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/alumni/stories')  # Redirect to the product list page after successful creation
    else:
        form = AlumniForm()
    return render(request, 'form.html', {'form': form})


def update(request, p_id):
    a = Alumni.objects.get(pk=p_id)
    if request.method == 'POST':
        form = AlumniForm(request.POST,request.FILES, instance=a)
        if form.is_valid():
            form.save()
            return redirect('/alumni/stories')  # Redirect to the product list page after successful update
    else:
        form = AlumniForm(instance=a)
    return render(request, 'form.html', {'form': form})
def delete(request,p_id):
    Alumni.objects.get(pk=p_id).delete()
    return redirect('/alumni/stories')

def alumni_association(request):
    alumni_association =Alumni_Association.objects.all()
    return render(request, 'alumni_association.html', {'alumni_association': alumni_association})


