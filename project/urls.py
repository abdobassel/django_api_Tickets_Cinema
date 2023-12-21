
from django.contrib import admin
from django.urls import path,include
from tickets import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapi/', views.noModelNoRest,),
    path('dajnagomodelnorest/',views.modelNoRest),
     path('core/', include('core.urls',)), 
     # rest 1 fbv def post and get list
    path('rest/fbvlist/', views.FbvList),
     
    
      path('api-auth/', include('rest_framework.urls')),
     

]
