from django.shortcuts import render



def login_view(request):
    if request.user.is_authenticated:
        msg=f'user is authenticated as {request.user.username}'
    else:
        msg='user not authenticated'
    return render(request,'accounts/login.html',{'msg':msg})

# def logout_view(request):
#     return

def singup_view(request):
    return render(request,'accounts/singup.html')