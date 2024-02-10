from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View

def home(request):
    return render(request, 'WebCheApp/home.html')

def logOut(request):
    logout(request)
    return redirect("home")

def logIn(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            userpassword = form.cleaned_data.get("password")
            user = authenticate(username=username, password=userpassword)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                for msg in form.error_messages:
                    messages.error(request, form.error_messages[msg])
                return render(request, "WebCheApp/logIn.html", {"form": form})
    form = AuthenticationForm()
    return render(request, "WebCheApp/logIn.html", {"form": form})

class registerForm(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'WebCheApp/register.html', {'form':form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request, 'WebCheApp/register.html', {'form':form})