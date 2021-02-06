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

def MemeListView(request):
    form = PostMeme()
    if request.method == 'POST':
        form = PostMeme(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    meme_list = Meme.objects.all().order_by('-date_created')
    paginator = Paginator(meme_list, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/index.html', {'form' : form, 'page_obj': page_obj})