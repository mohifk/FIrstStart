from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login


def login_view(request):
    # if request.user.is_authenticated:
    #     msg=f'user is authenticated as {request.user.username}'
    # else:
    #     msg='user not authenticated'
    # return render(request,'accounts/login.html',{'msg':msg})
    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request,'accounts/login.html')
    
# def logout_view(request):
#     return

def singup_view(request):
    return render(request,'accounts/singup.html')