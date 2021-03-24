from django.shortcuts import render, redirect
from .models import Show
from datetime import datetime

def index(request):
    return redirect('/shows')

def tv_shows(request):
    headings = ['ID', 'Network', 'Release Date', 'Actions']
    context = {
        'headings': headings,
        'all_shows': Show.objects.all()
    }
    return render(request, 'tv_shows.html', context)

def create_shows(request):
    return render(request, 'create_shows.html')

def process_shows(request):
    shows = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
    return redirect(f'/shows/{shows.id}')

def display_shows(request, id):
    context = {
        'new_shows': Show.objects.get(id=id),
    }
    return render(request, 'display_shows.html', context)

def edit_shows(request, id):
    context = {
        "tv_show": Show.objects.get(id=id),
    }
    return render(request, 'edit_shows.html', context)

def update_shows(request, id):
    tv_show = Show.objects.get(id=id)
    tv_show.title=request.POST['title']
    tv_show.network=request.POST['network']
    tv_show.release_date=request.POST['release_date']
    tv_show.desc=request.POST['desc']
    tv_show.save()
    return redirect(f'/shows/{tv_show.id}')

def delete_shows(request, id):
    tv_shows = Show.objects.get(id=id)
    tv_shows.delete()
    return redirect('/shows')