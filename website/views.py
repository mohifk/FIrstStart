from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from website.forms import ContactForm, NameForm,NewsletterForm

from django.contrib import messages
from django.shortcuts import redirect
def view_404(request, exception=None):
    messages.add_message(request,messages.SUCCESS,'Sorry Dude It will be available soon')
       
    
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/') # or redirect('name-of-index-url')
def Home_page_view(request):
    return render(request,'website_temp/index.html')
def about_view(request):
    return render(request ,'website_temp/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact=form.save(commit=False)
            Contact.name='unknown'
            Contact.save()
            
            messages.add_message(request,messages.SUCCESS,'OK Dude your tiket submit SUCCESS')
        else:
            messages.add_message(request,messages.ERROR,'Sorry Dude your tiket dident submit')
    form = ContactForm()
    return render(request,'website_temp/contact.html',{'form':form})

    
def elements_view(request):
    return render(request,'website_temp/elements.html')


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



