from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = 'home'
    template_name = "application/index.html"
