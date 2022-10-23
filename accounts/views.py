from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
def login_view(request):
    # if request.user.is_authenticated:
    #     msg=f'user is authenticated as {request.user.username}'
    # else:
    #     msg='user not authenticated'
    # return render(request,'accounts/login.html',{'msg':msg})
    #-------------------------------------------------------------------
    # if request.method == 'POST' :
    #     username=request.POST['username']
    #     password=request.POST['password']
    #     user=authenticate(request,username=username,password=password)
    #     if user is not None:
    #         login(request,user)
    #         return redirect('/')
    # return render(request,'accounts/login.html')  
    #---------------------------------------------------------------------------------
    if not request.user.is_authenticated:    
        if request.method == 'POST' :
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username=request.POST['username']
                password=request.POST['password']
                user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.add_message(request,messages.SUCCESS,'OK Dude you are login')
                return redirect('/')

        form=AuthenticationForm()
        context={'form':form}        
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')



@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'you are logout')
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST' :
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'OK Dude your signup succses please login')
                #return reverse('accounts:login')
                return redirect('/')
        form = UserCreationForm()
        context={'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')
