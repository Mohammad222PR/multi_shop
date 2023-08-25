from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Home(TemplateView):
    template_name = 'home/index.html'


    def get_contect_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        self.request.session.get('my_name', 'gust')

        
        return context