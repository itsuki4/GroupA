
from harada.forms import InquiryForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

def index(request):
    return render(request, 'diary/index.html')

class IndexView(generic.TemplateView):
    template_name="diary/index.html"

class InquiryView(generic.FormView):
    template_name = "diary/inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('harada:inquiry')