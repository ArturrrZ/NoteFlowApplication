from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
# Create your views here.

def old(request):
    return JsonResponse("INDEX",safe=False)

@api_view(["GET"])
def index(request):
    list=[{"id":1},{"id":2},{"id":3}]
    return Response(list)

@api_view(["GET"])
def notes(request):
    notes=Note.objects.all()
    return Response(notes)