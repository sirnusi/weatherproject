from django.urls import path
from . import views
urlpatterns = [
    path('', views.NoteList.as_view(), name='note-list'),
    #path('<slug:slug>/')
]
