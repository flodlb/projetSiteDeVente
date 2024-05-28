@login_required(login_url="accounts/login")
def home(request):
    return render(request, "polls/home.html")
