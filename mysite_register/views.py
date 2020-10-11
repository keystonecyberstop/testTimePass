from django.shortcuts import render
from django.views.generic import ListView
from .models import Entry

class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'

    # def get_context_data(self, **kwargs):
    #     print(kwargs)
    #     context = super().get_context_data(**kwargs)
    #     print('>>>>>>>>>>>')
    #     print(context)
    #     print('>>>>>>>>>>>')
    #     return context
    
# def home(request):
#     """
#     docstring
#     """
#     context = {
#         'entry_list' : Entry.objects.all()
#     }
#     return render(request, 'entries/index.html', context=context)