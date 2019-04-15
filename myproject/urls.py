"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from myapp.views import display_album_songs, show_genres
from one2one.views import display_car_engine, show_country
from m2m.views import display_groups
from learnqueryset.views import home_view
from learnforms.views import user_login, user_email, learn_manager
from learnauthentication.views import home
from django.contrib.auth import views as auth_views
from learntemplates.views import learn_template
from learnalltopics.views import learn_pagination, learn_serializers, send_email
from searchusers.views import search_user
from cmcas.views import DisplayBooks, CreateBook, UpdateBook, DeleteBook, UserLogin, learn_custom_filters, BookDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', user_login),
    url(r'^url/$', user_email),
    url(r'^manager/$', learn_manager),
    url(r'^album/$', display_album_songs, name='album'),
    url(r'^engine/$', display_car_engine, name='engine'),
    url(r'^group/$', display_groups, name='group'),
    url(r'^genres/$', show_genres),
    url(r'^country/clinic/subclinic/$', show_country),
    url(r'^home/$', home_view, name='home'),
    url(r'^templates/$', learn_template),
    url(r'^hom/$', home, name='hom'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^pagination/$', learn_pagination),
    url(r'^serialization/$', learn_serializers),
    url(r'^send-email/$', send_email),
    url(r'^search/$', search_user),
    url(r'^list/$', DisplayBooks.as_view(), name='list'),
    url(r'^create/$', CreateBook.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', UpdateBook.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteBook.as_view(), name='delete'),    
    url(r'^loginform/$', UserLogin.as_view(), name='login'),
    url(r'^custom-filters/$', learn_custom_filters, name='custom-filters'),
    url(r'^detail/(?P<pk>\d+)/$', BookDetailView.as_view(), name='detail'),
]
