from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('tasks/',views.TaskList.as_view(),name='tasks'),
    path('update/<int:pk>/',views.UpdateTask.as_view(),name='update'),
    path('delete/<int:pk>/',views.DeleteTask.as_view(),name='delete'),
    path('create/',views.CreateTask.as_view(),name='add'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'), 
    path('',views.Login.as_view(),name='login'),  
    path('register/',views.Register.as_view(),name='register'),  
]