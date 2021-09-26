
import logging
from harada.forms import InquiryForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'diary/index.html')

class IndexView(generic.TemplateView):
    template_name="diary/index.html"

class InquiryView(generic.FormView):
    template_name = "diary/inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('harada:inquiry')
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary
class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary/diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries


