
from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('index/', views.index, name="index"),

    path('download_pdf/', views.download_pdf, name="download_pdf"),
    path('after/', views.after, name="after"),
    ]