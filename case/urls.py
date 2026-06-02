from django.contrib import admin
from django.urls import path
from caseapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),

    path('shots/', views.shots),

    path('designers/', views.designers),

    path('teams/', views.teams),

    path('community/', views.community),

    path('designs/', views.designs),

    path('signup/', views.signup),
]