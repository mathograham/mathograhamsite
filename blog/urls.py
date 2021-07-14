from django.urls import path
from . import views


#Tells django what to do with appendage to site's url
#first string in path is the appendage,
#second element is the view in views.py(must be created)
#third element is the name. Name used in html when calling django code
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
