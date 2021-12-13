from django.urls import path
from . import views
urlpatterns = [
    path('', views.NoteList.as_view(), name='note-list'),
    path('<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
    path('create/', views.NoteCreate.as_view(), name='note-create'),
    path('list/', views.UserNote.as_view(), name='user-review-note'),
    path('search/', views.NoteSearch.as_view(), name='note-search'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/create/', views.CategoryCreate.as_view(), name='category-create'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    
]
