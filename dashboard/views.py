import django
from dashboard.forms import PostMeme
from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.http import HttpResponseRedirect
from .models import Meme
from django.utils import timezone
from django.core.paginator import Paginator

# class MemeListView(FormView, ListView):
#     template_name = 'dashboard/index.html'
#     model = Meme
#     form_class = PostMeme

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form':form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('/success/')

    #     return render(request, self.template_name, {'form': form})


    # template_name = 'dashboard/index.html'
    # model = Meme
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from memeAPI.serializers import MemeSerializers


class MemeListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard/index.html'
    form = PostMeme()

    def get(self, request):
        meme_list = Meme.objects.all().order_by('-date_created')
        paginator = Paginator(meme_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return Response({'page_obj':page_obj})

    def post(self, request, *args, **kwargs):
        form = PostMeme(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

    # def post(self, request, pk):
    #     profile = get_object_or_404(Meme, pk=pk)
    #     serializer = MemeSerializers(profile, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'memes': profile})
    #     serializer.save()
    #     return HttpResponseRedirect('/')


# def MemeListView(request):
#     form = PostMeme()
#     if request.method == 'POST':
#         form = PostMeme(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')

#     meme_list = Meme.objects.all().order_by('-date_created')
#     paginator = Paginator(meme_list, 100)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'dashboard/index.html', {'form' : form, 'page_obj': page_obj})