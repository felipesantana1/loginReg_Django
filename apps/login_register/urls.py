from django.conf.urls import url
import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'create$', views.create),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout)

]