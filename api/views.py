import json

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
    all_notes=Note.objects.all()
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

@csrf_exempt
def edit_note(request,id):
    # serializer = NoteSerializer(instance=note, data=body)
    # if serializer.is_valid():
    #     serializer.save()
    if request.method == 'PUT':
        # remove from cart
        data = json.loads(request.body)
        body=data.get("body")
        if body is not None:
            try:
                # Find the note by id
                note = Note.objects.get(pk=id)
                # Update the body of the note
                note.body = body
                # Save the changes to the database
                note.save()
                # Return a success response
                return JsonResponse({"success": "Note updated successfully"}, status=200)
            except ObjectDoesNotExist:
                # If the note does not exist, return an error response
                return JsonResponse({"error": "Note does not exist"}, status=404)
        else:
            # If body is not provided in the request, return an error response
            return JsonResponse({"error": "No body provided"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)