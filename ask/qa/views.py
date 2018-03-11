from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from qa.models import Question, Answer


def pagination(qs, request, baseurl):
    try:
        limit = int(request.GET.get('limit', 10))
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    if limit > 100:
        limit = 10
    paginator = Paginator(qs, limit)
    paginator.baseurl = baseurl
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator

def new(request):
    question = Question.objects.new()
    page, paginator = pagination(question, request, '/?page=')
    context = {'questions': page.object_list, 'paginator': paginator, 'page': page, }
    return render(request, 'list.html', context)

def popular(request):
    question = Question.objects.popular()
    page, paginator = pagination(question, request, '/popular/?page=')
    context = {'questions': page.object_list, 'paginator': paginator, 'page': page, }
    return render(request, 'popular.html', context)

def question(request, index):
    quest = get_object_or_404(Question, pk=index)
    answers = Answer.objects.filter(question = quest)
    context = {'question': quest, 'answers': answers }
    return render(request, 'question.html', context)

def test(request, *args, **kwargs):
    return HttpResponse('OK')
