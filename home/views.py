from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, timedelta

def credits(request):
  content = 'Nick\nLuke\nKyle\n'
  return HttpResponse(content, content_type='text/plain')

def news(request):
  data = {
    'news': [
      "RiffMates has news page!",
      "RiffMates has credits page!",
    ]
  }
  return render(request, 'news.xhtml', data)

def news_advanced(request):
  today = date.today()
  before1 = today - timedelta(days=1)
  before2 = today - timedelta(days=2)
  data = {
    'news': [
      (today, "Advanced news added! It's the best news!"),
      (before1, "RiffMates has news page!"),
      (before2, "RiffMates has credits page!"),
    ]
  }
  return render(request, 'adv_news.xhtml', data)