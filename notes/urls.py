from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='notes.list'),
    path('notes/<int:pk>', views.NoteItemView.as_view(), name='notes.detail'),
    path('notes/<int:pk>/edit', views.NoteUpdateView.as_view(), name='notes.edit'),
    path('notes/new', views.NoteCreateView.as_view(), name='notes.new'),
    path('notes/<int:pk>/delete', views.NoteDeleteView.as_view(), name='notes.delete')
]