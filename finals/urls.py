"""
URL configuration for finals project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from finals import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signaction,name='sign'),
    path('login/',views.loginuser),
    path('home',views.homepage,name='home'),
    path('sofa/',views.sofas,name='sofa'),
    path('bedset/',views.bedsets,name='beds'),
    path('chairs/',views.chairss,name='chair'),
    path('ContactUs/',views.ContactUss,name='contact'),
    path('details/<str:pk>',views.details,name='details'),
    path('detail2/<str:pk>',views.detail2,name='detail2'),
    path('detail3/<str:pk>',views.detail3,name='detail3'),   
    path('cart/<str:pk>',views.cart,name='cart'),
     path('addtocart/<str:product_id>',views.addtocart,name='addtocart'),
    
       path('Aboutus/',views.Aboutus,name='Aboutus'),

     path('signout/',views.signout),
   
  
       
       
  
   

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
