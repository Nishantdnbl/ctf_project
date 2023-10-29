from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('submit', views.submit, name='submit'),
    path('flg3', views.flg3, name='flg3'),
    path('flag4', views.flag4, name='flag4'),
    path('challange_1:', views.challange_1, name='challange_1'),
    path('challange_2:', views.challange_2, name='challange_2'),
    path('challange_3:', views.challange_3, name='challange_3'),
    path('challange_4:', views.challange_4, name='challange_4'),
    path('challange_5:', views.challange_5, name='challange_5'),
]

