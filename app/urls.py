from django.urls import path
from .views import ListView,CreateView,RetrieveView,UpdateView,DestroyView

urlpatterns = [
    path('list/', ListView.as_view(), name='list'),
    path('create/', CreateView.as_view(), name='create'),
    path('retrive/<int:pk>/', RetrieveView.as_view(), name='retrive'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update'),
    path('destroy/<int:pk>/', DestroyView.as_view(), name='destroy'),
]