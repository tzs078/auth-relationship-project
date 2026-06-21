from django.urls import path
from new_app.views import *


urlpatterns = [
    path('', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/',logout_view,name='logout_view'),

    path('dashboard/', dashboard, name='dashboard'),
    path('task_list/', task_list, name='task_list'),
    path('task_add/', task_add, name='task_add'),
    path('task_update/<str:id>/', task_update , name='task_update'),
]