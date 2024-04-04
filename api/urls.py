from django.urls import path
from . import views

urlpatterns = [
    path('old',views.old,name="old"),
    path('',views.index,name="index"),
    path('notes/',views.notes,name="notes"),
    path('note/edit/<int:id>/',views.edit_note,name="edit"),
    path('note/<int:id>/',views.note,name="note"),
    path('note/create_note',views.create_note,name='create_note'),
    path('note/delete/<int:id>',views.delete_note,name='delete_note')
    ]