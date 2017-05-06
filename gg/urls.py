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
    url(r'^about/(\d+)/$', views.about_detail),
    url(r'^product/$', views.product_index, name="product"),
    # url(r'^facility/$', views.faclity_index, name="faclity"),
    url(r'^jobs/$', views.jobs_index, name="jobs"),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^about_sample/$', views.about_sample, name="contact"),
    url(r'^success/$', views.success, name="success"),
    url(r'^facility/(\d+)/$',views.faclity_index),
    url(r'information/$', views.information),
    url(r'^information_detail/(?P<aid>\d+)$', views.information_detail),
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


    url(r'^r/product$',views.product_view),
    url(r'^r/getproduct$', views.ajax_get_product),
    url(r'^r/editproduct$', views.edit_product),
    url(r'^r/productclass$', views.productclass_view),
    url(r'^r/getproductclass$', views.ajax_get_productclass),
    url(r'^r/delproductclass$', views.del_productclass),
    url(r'^r/addproductclass', views.add_productclass),

    url(r'^r/facility$', views.facility_view),
    url(r'^r/getfacility$', views.ajax_get_facility),
    url(r'^r/editfacility$', views.edit_facility),
    url(r'^r/facilityclass$', views.facilityclass_view),
    url(r'^r/getfacilityclass$', views.ajax_get_facilityclass),
    url(r'^r/delfacilityclass$', views.del_facilityclass),
    url(r'^r/addfacilityclass', views.add_facilityclass),

    url(r'^r/certificate$', views.certificate_view),
    url(r'^r/getcertificate$', views.ajax_get_certificate),
    url(r'^r/editcertificate$', views.edit_certificate),
    url(r'^r/certificateclass$', views.certificateclass_view),
    url(r'^r/getcertificateclass$', views.ajax_get_certificateclass),
    url(r'^r/delcertificateclass$', views.del_certificateclass),
    url(r'^r/addcertificateclass', views.add_certificateclass),

    url(r'^r/filebrowser$', views.filebrowser),
    url(r'^r/login$', views.login_backend),
    url(r'^r/logout$', views.logout),
    url(r'^r/xxxuser$', views.add_user),
    url(r'^r/deluser$', views.del_user),
    url(r'^r/user$', views.edit_user),
    url(r'^r/getuser$', views.ajax_get_user),

    url(r'^r/aboutclass$', views.aboutclass_view),
    url(r'^r/getaboutclass$', views.ajax_get_aboutclass),
    url(r'^r/delarticleclass$', views.del_articleclass),
    url(r'^r/addaboutclass', views.add_aboutclass),
    url(r'^r/editabout$', views.edit_about),
    url(r'^r/delaboutclass$', views.del_aboutclass),

    url(r'^r/contactus$', views.contactus_view),
    url(r'^r/get_contact$', views.ajax_get_contact),
    url(r'^r/del_contact$', views.ajax_del_contact),

    url(r'^r/joinus$', views.join_view),
    url(r'^r/getjoin$', views.ajax_get_join),
    url(r'^r/editjoin$', views.edit_join),



]

