from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
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
                return redirect('/')

        form=AuthenticationForm()
        context={'form':form}        
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')



@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def singup_view(request):
    return render(request,'accounts/singup.html')