from django.urls import path
from . import views
urlpatterns = [
    path('', views.NoteList.as_view(), name='note-list'),
    path('<int:pk>/details/', views.NoteDetail.as_view(), name='note-detail'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
]
