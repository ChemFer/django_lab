from django.urls import path, include
from .views import index, add, get, updateNews, deleteNews

urlpatterns = [
    path('', index, name="view_news"),
    path('add/', add, name="add"),
    path('<int:id>/', get, name='get'),
    path('update_news/<int:id>/', updateNews, name="update_news"),
    path('delete_news/<str:id>/', deleteNews, name="delete_news"),

]
