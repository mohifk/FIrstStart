
from django.urls import path
from website.views import *

urlpatterns = [

    path ('',Home_page_view),
    path ('about/',about_view),
    path ('contact',contact_view)
]