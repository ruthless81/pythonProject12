from django import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('cars/', views.CarListCreateView.as_view(), name='car-list'),
    path('cars/<int:pk>/', views.CarRetrieveUpdateDestroyView.as_view(), name='car-detail'),
    path('animals/', views.AnimalListCreateView.as_view(), name='animal-list'),
    path('animals/<int:pk>/', views.AnimalRetrieveUpdateDestroyView.as_view(), name='animal-detail'),
]
