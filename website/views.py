from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from website.forms import NameForm
from website.models import Contact

def Home_page_view(request):
    return render(request,'.\website_temp\index.html')
def about_view(request):
    return render(request ,'.\website_temp\\about.html')
def contact_view(request):
    return render(request,'.\website_temp\contact.html')
def elements_view(request):
    return render(request,'.\website_temp\elements.html')

def test_view(request):
    if request.method == 'POST' :
        form = NameForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name,subject,email,message)
            return HttpResponse('done')
        else:
            return HttpResponse('note valid')
    
    form = NameForm()

    return render(request,'test.html',{'form':form})
    