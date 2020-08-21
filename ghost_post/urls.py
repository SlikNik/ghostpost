"""ghost_post URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from ghost import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('sorted/', views.sort, name='sorted'),
    path('boasts/', views.boast, name='boast'),
    path('roasts/', views.roast, name='roast'),
    path('addpost/', views.create_post, name='createpost'),
    path('upvote/<int:id>/', views.up_vote, name='upvote'),
    path('downvote/<int:id>/', views.down_vote, name='downvote'),
    path('post/<str:secret>/', views.post, name='post'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('admin/', admin.site.urls),
]
