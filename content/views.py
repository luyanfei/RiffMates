from django.shortcuts import render, redirect
from django.core.mail import send_mail
from content.forms import CommentForm
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
