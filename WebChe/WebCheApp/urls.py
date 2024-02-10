from django.urls import path
from WebCheApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.registerForm.as_view(), name='Register'),
    path('logOut', views.logOut, name='LogOut'),
    path('LogIn', views.logIn, name='LogIn'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)