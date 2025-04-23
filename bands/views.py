from django.shortcuts import render, get_object_or_404
from bands.models import Musician

def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    return render(request, 'musician.xhtml', {'musician': musician})


