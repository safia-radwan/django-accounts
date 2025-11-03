from django.shortcuts import render,redirect

# Create your views here.\
from . models import profile
from django.http import HttpResponseRedirect
from . forms import profileform,signupform,userform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username =username,password=password)
            login(request, user)
            return redirect('/accounts/profile/')
    else:
        form =signupform()
    return render(request, 'registration/signup.html', {'form': form})    


def user_profile (request):
    # objects=profile.objects.all()
    pro=profile.objects.get(user = request.user)
    return render(request, "profile/profile.html", {"profile": pro})


def update_profile(request):
    pro=profile.objects.get(user = request.user)
    if request.method == 'POST':
        print('before Post')
        user_from=userform(request.POST,instance=request.user)
        profile_from=profileform(request.POST,instance=pro)
        if user_from.is_valid() and profile_from.is_valid():
            print("is invalid")
            profile_from.save()
            user_from.save()
            return redirect('/accounts/profile')
    else:
        print('not valid')
        user_from=userform(instance=request.user)
        profile_from=profileform(instance=pro)
    return render(request, "profile/update_profile.html", {
        'user_form':user_from,
        'profile_form':profile_from,
    })

