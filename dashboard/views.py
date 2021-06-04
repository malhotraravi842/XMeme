from dashboard.forms import PostMeme
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Meme
from django.core.paginator import Paginator
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


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
    

# class MemeListView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'dashboard/index.html'
#     form = PostMeme()

#     def get(self, request):
#         meme_list = Meme.objects.all().order_by('-date_created')
#         paginator = Paginator(meme_list, 10)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         return Response({'page_obj':page_obj})

#     def post(self, request, *args, **kwargs):
#         form = PostMeme(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')

#         return render(request, self.template_name, {'form': form})