from django.urls import path
from . import views

urlpatterns = [
    path('old',views.old,name="old"),
    path('',views.index,name="index"),
    path('notes/',views.notes,name="notes"),
    path('note/edit/<int:id>/',views.edit_note,name="edit"),
    path('note/<int:id>/',views.note,name="note"),
    ]