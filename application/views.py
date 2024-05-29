from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic


# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = 'home'
    template_name = "application/index.html"
    
@login_required(login_url='home')
def list_view(request):
    return render(request, 'application/home.html')
    
@login_required(login_url='compte:login')
def home(request):
    return render(request,"application/home.html")
