from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.views.generic import TemplateView, RedirectView, DetailView, UpdateView
from .forms import HomeForm
from .models import Url
from url.constants import DOMAIN_NAME

# Create your views here.

class HomeView(TemplateView):
    '''Home page view'''
    slug_number = 0
    template_name = 'url/Home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            if Url.objects.filter(url=url): # Chceking if that url is allready in  DB
                url_result = Url.objects.get(url=url)
            else: # Creating new instance
                HomeView.slug_number += 1
                url_result = Url.objects.create(
                url=url, 
                shorted_url=DOMAIN_NAME + str(HomeView.slug_number),
                )
        
        args = {'form':form, 'url':url_result}
        return render(request, self.template_name, args)


def redirect_original(request, pk):
    '''Redirection to original url'''
    url = Url.objects.get(pk=pk).url # Getting url from instance
    return redirect(url)