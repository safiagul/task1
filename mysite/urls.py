from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.index, name='index'),
  path('headings/', views.headings, name='headings'),
  path('bold_italic/', views.bold_italic, name='bold_italic'),
  path('unordered_list/', views.unordered_list, name='unordered_list'),
  path('simple_table/', views.simple_table, name='simple_table'),
  path('sdsu_image/', views.sdsu_image, name='sdsu_image'),
  path('ip_api/', views.ip_api, name='ip_api'),
]
