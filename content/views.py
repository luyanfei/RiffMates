from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from content.forms import CommentForm, SeekingAdForm
from content.models import SeekingAd, MusicianBandChoice

def comment(request):
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            message = f'Name: {name}\nComment: {comment}'
            send_mail('Received comment', message, 'from@example.com', ['to@example.com'], fail_silently=False)
            return redirect('comment_accepted')
    data = {'form': form}
    return render(request, 'comment.xhtml', data)

def comment_accepted(request):
    data = {
        'content': 'Thank you for your comment. We will review it shortly.'
    }
    return render(request, 'general.xhtml', data)

def list_ads(request):
    data = {
        'seeking_musician': SeekingAd.objects.filter(
            seeking=MusicianBandChoice.MUSICIAN
        ),
        'seeking_band': SeekingAd.objects.filter(
            seeking=MusicianBandChoice.BAND
        )
    }
    return render(request, 'list_ads.xhtml', data)

@login_required
def seeking_ad(request, ad_id=0):
    if request.method == 'GET':
        if ad_id == 0:
            form = SeekingAdForm()
        else:
            ad = get_object_or_404(SeekingAd, id=ad_id, owner=request.user)
            form = SeekingAdForm(instance=ad)
    if request.method == 'POST':
        if ad_id == 0:
            form = SeekingAdForm(request.POST)
        else:
            ad = get_object_or_404(SeekingAd, id=ad_id, owner=request.user)
            form = SeekingAdForm(request.POST, instance=ad)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.owner = request.user
            ad.save()
            return redirect('list_ads')
    data = {'form': form}
    return render(request, 'seeking_ad.xhtml', data)
