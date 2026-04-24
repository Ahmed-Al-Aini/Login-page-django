from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', views.login, name='registration'),
    # path('logout/', views.logout, name='logout'),
]
