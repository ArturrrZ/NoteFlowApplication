from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
# Create your views here.

def old(request):
    return JsonResponse("INDEX",safe=False)

@api_view(["GET"])
def index(request):
    list=[{"id":1},{"id":2},{"id":3}]
    return Response(list)

@api_view(["GET"])
def notes(request):
    # notes=Note.objects.all().values("title","body")
    all_notes=Note.objects.all()
    serializer=NoteSerializer(all_notes,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def note(request,id):
    note=Note.objects.get(pk=id)
    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)