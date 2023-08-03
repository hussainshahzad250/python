from django.urls import path
from tutorials import views

app_name = 'tutorials'

urlpatterns = [

    path('api/tutorials', views.tutorial_list, name='Tutorial List'),
    path('api/tutorials/<int:pk>/', views.tutorial_detail, name='Tutorial Detail'),
    path('api/tutorials/published', views.tutorial_list_published, name='Tutorial'),
    path('api/employees', views.employee_list, name='Employee'),

]