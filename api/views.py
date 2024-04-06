import json
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from django.core.exceptions import ObjectDoesNotExist
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
    all_notes=Note.objects.all().order_by("-updated")
    serializer=NoteSerializer(all_notes,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def note(request,id):
    try:
        note=Note.objects.get(pk=id)
    except ObjectDoesNotExist:
        return JsonResponse({"error":"does not exist"},status=404)
    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def edit_note(request,id):
        print(id)
    # serializer = NoteSerializer(instance=note, data=body)
    # if serializer.is_valid():
    #     serializer.save()
    # remove from cart
        data = json.loads(request.body)
        body=data.get("body")
        title=data.get('title')
        if body is not None:
            try:
                note = Note.objects.all().get(pk=id)
                note.body = body
                note.title=title
                note.save()
                return JsonResponse({"success": "Note updated successfully"}, status=200)
            except ObjectDoesNotExist:
                # If the note does not exist, return an error response
                return JsonResponse({"error": "Note does not exist"}, status=404)
        else:
            # If body is not provided in the request, return an error response
            return JsonResponse({"error": "No body provided"}, status=400)




@api_view(["POST"])
def create_note(request):
    data=json.loads(request.body)
    note=Note.objects.create(
        title=data["note"]["title"],
        body=data["note"]["body"]
    )
    notes = Note.objects.all().order_by("-updated")
    serializerr = NoteSerializer(notes, many=True)
    return Response(serializerr.data, status=200)

@api_view(["DELETE"])
def delete_note(request,id):
    try:
        note=Note.objects.all().get(pk=id)
    except ObjectDoesNotExist:
        return Response("forbidden",status=404)
    note.delete()
    notes=Note.objects.all()
    serializerr=NoteSerializer(notes,many=True)
    return Response(serializerr.data,status=200)