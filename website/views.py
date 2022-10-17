from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from website.forms import ContactForm, NameForm,NewsletterForm
from website.models import Contact
from django.contrib import messages
def Home_page_view(request):
    return render(request,'.\website_temp\index.html')
def about_view(request):
    return render(request ,'.\website_temp\\about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.name='unknown'
            form.save()
            
            messages.add_message(request,messages.SUCCESS,'OK Dude your tiket submit SUCCESS')
        else:
            messages.add_message(request,messages.ERROR,'Sorry Dude your tiket dident submit')
    form = ContactForm()
    return render(request,'.\website_temp\contact.html',{'form':form})

    
def elements_view(request):
    return render(request,'.\website_temp\elements.html')


def test_view(request):
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('note valid')
    
    form = ContactForm()

    return render(request,'test.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST' :
        form=NewsletterForm(request.POST)    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
