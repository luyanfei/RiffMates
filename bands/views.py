from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
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

@login_required
def restricted_page(request):
    data = {
        'title': 'Restricted Page',
        'content': '<h1>This is a restricted page</h1>'
    }
    return render(request, 'general.xhtml', data)

@login_required
def musician_restricted(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    profile = request.user.userprofile
    allowed = False
    if profile.musician_profiles.filter(id=musician.id).exists():
        allowed = True
    else:
        musician_profiles = set(profile.musician_profiles.all())
        for band in musician.band_set.all():
            band_musicians = set(band.musicians.all())
            if musician_profiles.intersection(band_musicians):
                allowed = True
                break
    if not allowed:
        raise Http404('Permission denied')
    
    content = f"""
    <h1>Musician Page: {musician.last_name}</h1>
    <p>{musician.first_name}</p>
    <p>{musician.last_name}</p>
    <p>{musician.birth}</p>
    """
    data = {
        'title': 'Restricted musician',
        'content': content,
    }
    return render(request, 'general.xhtml', data)