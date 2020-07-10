from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question


def test(request, *args, **kwargs):
    from django.http import HttpResponse
    return HttpResponse('OK')


def new(request):

    # for i in range(20):
    #     Question.objects.create(title="test_title_"+str(i), text='test_text_'+str(i))
    # return test('LOL')

    questions = Question.objects.new()

    # from django.urls import reverse
    # paginator.baseurl = reverse('new')

    # if paginator.count == 0:
    #     return test('LOL')

    page, paginator = paginate(request, questions)

    return render(request, '10_qustions.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
    })


def popular(request):
    questions = Question.objects.popular()
    page, paginator = paginate(request, questions)
    return render(request, 'popular_questions.html', {
        'page': page,
        'paginator': paginator
    })


def detail(request, id):
    question = get_object_or_404(Question, id=id)
    return render(request, 'detail.html', {
        'question': question,
    })


def paginate(request, qs):

    # try:
    #     limit = int(request.GET.get('limit', 10))
    # except ValueError:
    #     limit = 10
    # if limit > 100:
    #     limit = 10

    paginator = Paginator(qs, 10)
    page = request.GET.get('page', 1)

    try:
        page = paginator.page(page)

    except PageNotAnInteger:
        page = paginator.page(1)

    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page, paginator
