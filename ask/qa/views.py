from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from qa.models import Question, Answer
from .forms import AskForm, AnswerForm


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
    if request.method == "POST":
        form = AnswerForm(request.POST, quest.pk)
        if form.is_valid():
            form.save(quest.pk)
            url = quest.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    answers = Answer.objects.filter(question = quest)
    context = {'question': quest, 'answers': answers, 'form' : form }
    return render(request, 'question.html', context)

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    context = {'form' : form }
    return render(request, 'ask.html', context)

def test(request, *args, **kwargs):
    return HttpResponse('OK')
