from django.shortcuts import render



def login_view(request):
    return render(request,'accounts/login.html')

# def logout_view(request):
#     return

def singup_view(request):
    return render(request,'accounts/singup.html')