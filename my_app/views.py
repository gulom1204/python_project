from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    return HttpResponse("<h1>Hello world</h1>")

def post(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]

    else:
        form = UserForm()

    return render(request, "my_app/post.html", {'form': form})
