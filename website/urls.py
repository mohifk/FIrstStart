
from django.urls import path
from website.views import *

app_name='website'

urlpatterns = [

    path ('',Home_page_view,name='index'),
    path ('about/',about_view,name='about'),
    path ('contact/',contact_view,name='contact'),
    path ('elements/',elements_view,name='elements'),
    path ('test/',test_view,name='test'),
    path ('newsletter_view/',newsletter_view,name='newsletter'),
]


# handler404 = 'my_app.views.handler404'