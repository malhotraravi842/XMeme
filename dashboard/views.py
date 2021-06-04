from dashboard.forms import PostMeme
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Meme


def homepage(request):
    if request.method == 'POST':
        form = PostMeme(request.POST, request.FILES)
        if form.is_valid:
            form.save()

        form = PostMeme()
        return HttpResponseRedirect('/')
    else:
        form = PostMeme()
    
    memes = Meme.objects.all().order_by('-date_created')

    return render(request, 'dashboard/index.html', {'form':form, 'memes': memes})



def delete_meme(request, id):
    if request.method == 'POST':
        meme = Meme.objects.get(pk=id)
        meme.delete()
        return HttpResponseRedirect('/')

def update_meme(request, id):
    if request.method == 'POST':
        meme = Meme.objects.get(pk=id)
        form = PostMeme(request.POST, request.FILES, instance=meme)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        meme = Meme.objects.get(pk=id)
        form = PostMeme(instance=meme)

    return render(request, 'dashboard/update.html', {'form': form})