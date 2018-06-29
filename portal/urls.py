from django.urls import include, path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    path('^search/?q=', views.index),
    re_path(r'^contact_form/$', views.contact),
    re_path(r'^search/$', views.searchres),
    path('index.html', views.index),
    path('index/', views.index),
    path('ss', views.terr),
]
