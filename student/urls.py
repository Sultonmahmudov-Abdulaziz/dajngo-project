from django.urls import path
from. import views



urlpatterns = [
    path('', views.index ,name='index'),
    path('category/<int:id>', views.category ,name='category'),
    path('airveys/<int:id>/', views.airveys, name='airveys'),

]