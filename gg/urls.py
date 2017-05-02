"""gg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about/$', views.about, name="about"),
    url(r'^product/$', views.product, name="product"),
    url(r'^facility/$', views.faclity, name="faclity"),
    url(r'^jobs/$', views.jobs, name="jobs"),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^about_sample/$', views.about_sample, name="contact"),
    url(r'^success/$', views.success, name="success"),


    url(r'^r/index$|^r/$|^r$', views.backend_index),

    url(r'^r/carousel$', views.edit_carousel),
    url(r'^r/addcarousel$', views.add_carousel),
    url(r'^r/delcarousel$', views.del_carousel),
    url(r'^r/getcarousel$',views.ajax_get_carousel),
    url(r'^r/gallery$',views.gallery),
    url(r'^r/getpictures$',views.ajax_get_pictures),
    url(r'^r/addpicture$',views.add_picture),
    url(r'^r/delpicture$',views.del_picture),

    url(r'^r/content$', views.content),
    url(r'^r/getcontent$', views.ajax_get_content),
    url(r'^r/editcontent$', views.edit_content),
    url(r'^r/articleclass$', views.articleclass_view),
    url(r'^r/getarticleclass$', views.ajax_get_articleclass),
    url(r'^r/delarticleclass$', views.del_articleclass),
    url(r'^r/addarticleclass', views.add_articleclass),


    url(r'^r/product$',views.content),
    url(r'^r/getproduct$', views.ajax_get_content),
    url(r'^r/editproduct$', views.edit_content),
    url(r'^r/productclass$', views.productclass_view),
    url(r'^r/getproductclass$', views.ajax_get_productclass),
    url(r'^r/delproductclass$', views.del_productclass),
    url(r'^r/addproductclass', views.add_productclass),


    url(r'^r/facility$', views.content),
    url(r'^r/getfacility$', views.ajax_get_content),
    url(r'^r/editfacility$', views.edit_content),
    url(r'^r/facilityclass$', views.facilityclass_view),
    url(r'^r/getfacilityclass$', views.ajax_get_facilityclass),
    url(r'^r/delfacilityclass$', views.del_facilityclass),
    url(r'^r/addfacilityclass', views.add_facilityclass),

    url(r'^r/filebrowser$', views.filebrowser),
    url(r'^r/login$', views.login_backend),
    url(r'^r/logout$', views.logout),
    url(r'^r/xxxuser$', views.add_user),
    url(r'^r/deluser$', views.del_user),
    url(r'^r/user$', views.edit_user),
    url(r'^r/getuser$', views.ajax_get_user),
]

