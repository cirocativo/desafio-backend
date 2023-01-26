from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('show/', views.show_transactions, name='show_transactions')
]