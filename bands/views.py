from django.shortcuts import render, get_object_or_404
from bands.models import Musician

def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    return render(request, 'musician.xhtml', {'musician': musician})

def musicians(request):
    musicians = Musician.objects.all().order_by('last_name')
    return render(request, 'musicians.xhtml', {'musicians': musicians})
