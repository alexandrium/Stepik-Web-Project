from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# from django.contrib.sessions import *
from .models import Question
from .forms import AskForm, AnswerForm, UserCreationForm
# from django.contrib.auth.forms import UserCreationForm


def signup(request):
    redirect_to = request.GET.get('next', '/')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect('new')
            return redirect(redirect_to)
            # return redirect('/popular/?page=3')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {
        'form': form,
    })


# def logout(request):
#     auth_views.logout(request)
#     return redirect('questions:index')


def new(request):

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

        if request.user.is_authenticated:
            form._user = request.user
            
        if form.is_valid():
            form.save(id)   # new strange logic in form.save, can be rew:
            #  answer = form.save(commit=False); answer.question_id = id; answer.save()
            # return HttpResponseRedirect(reverse(detail, kwargs={'id': id}))
            # return HttpResponseRedirect('/question/' + str(id) + '/')
            return redirect('detail', id=id)
    else:
        form = AnswerForm()
        # form = AnswerForm(initial={"question": id})

    question = get_object_or_404(Question, id=id)   # x3 SELECT from 3 tables; O_o

    return render(request, 'detail.html', {
        'question': question,
        # 'answers': question.answer_set.all()[:],
        'likes': question.likes.count(),
        # try: 'mylike': question.likes.filter(id=request.id, ??? )
        'form': form,
    })


# @login_required(login_url='login')
def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)

        if request.user.is_authenticated:
            form._user = request.user

        # form._user = request.user
        if form.is_valid():
            question = form.save()
            # return HttpResponseRedirect(reverse(detail, kwargs={'id': question.id}))
            return redirect('detail', id=question.id)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


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
