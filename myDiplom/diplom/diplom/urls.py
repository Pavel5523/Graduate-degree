"""
URL configuration for diplom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from flashcards import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.start, name='start'),
    path('admin/', admin.site.urls),
    path('signup/', views.signupuser, name='signupuser'),
    path('home/', views.home, name='home'),
    path('come/', views.come, name='come'),
    path('flashcard/', views.flashcard, name='flashcard'),
    path('create_flashcard/', views.create_flashcard, name='create_flashcard'),
    path('flashcard/<int:flashcard_pk>/delete', views.delete_flashcard, name='delete_flashcard'),
    # path('back_home/', views.back_home, name='back_home'),
    path('education/', views.education, name='education'),
    path('education/', views.next, name='next')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
