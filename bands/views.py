from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from bands.models import Musician

def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    return render(request, 'musician.xhtml', {'musician': musician})

def musicians(request):
    all_musicians = Musician.objects.all().order_by('last_name')
    max_number = request.GET.get('max', 2)
    paginator = Paginator(all_musicians, max_number)
    page_number = request.GET.get('page', 1)
    page_number = int(page_number)

    if page_number > paginator.num_pages:
        page_number = paginator.num_pages
    elif page_number < 1:
        page_number = 1

    page = paginator.page(page_number)
    data = {
        'musicians': page.object_list,
        'page': page,
    }

    return render(request, 'musicians.xhtml', data)
