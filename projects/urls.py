from django.urls import path
from projects import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.projects.as_view()),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)