from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse

from .models import Question
from .forms import AskForm, AnswerForm


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

    page = paginate(request, questions)

    return render(request, '10_qustions.html', {
        'page': page,
    })


def popular(request):
    questions = Question.objects.popular()
    page = paginate(request, questions)
    return render(request, 'popular_questions.html', {
        'page': page,
    })


# @require_GET
def detail(request, id):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save(id)
            return HttpResponseRedirect(reverse(detail, kwargs={'id': id}))
    else:
        form = AnswerForm()

    question = get_object_or_404(Question, id=id)

    return render(request, 'detail.html', {
        'question': question,
        # 'answers': question.answer_set.all()[:],
        'likes': question.likes.count(),
        # try: 'mylike': question.likes.filter(id=request.id, ??? )
        'form': form,
    })


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(reverse(detail, kwargs={'id': question.id}))
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form
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

    # В случае отсутствия вопросов получим пустую страницу О_о

    try:
        page = paginator.page(page)

    except PageNotAnInteger:
        page = paginator.page(1)

    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page
