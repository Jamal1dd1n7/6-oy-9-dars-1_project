from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from datetime import datetime
from .models import *
from .forms import *

def home(request: WSGIRequest):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'intex.html', context)

def course(request: WSGIRequest, course_id):
    lessons = Lesson.objects.all()
    context = {
        'lessons': lessons
    }
    return render(request, 'course.html', context)
    
def lesson(request: WSGIRequest, lesson_id):
    lesson = get_object_or_404(Lesson, id= lesson_id)
    comments = Comment.objects.filter(lesson_id=lesson_id)
    context = {
        'lesson': lesson,
        'form': CommentForm(),
        'comments': comments,
        'current_year': datetime.now().year
    }
    return render(request, 'lesson.html', context)
    
def add_lesson(request: WSGIRequest):

    if request.method == 'POST':
        form = LessonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = Lesson.objects.create(**form.cleaned_data)
            print(post, "qo'shildi!")

    form = LessonForm()
    context = {
        "form": form
    }
    return render(request, 'add_lesson.html', context)

def add_course(request: WSGIRequest):

    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = Course.objects.create(**form.cleaned_data)
            print(post, "qo'shildi!")
        else:
            print(form.errors)

    form = CourseForm()
    context = {
        "form": form
    }
    return render(request, 'add_course.html', context)

def comment_save(request: WSGIRequest, lesson_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            lesson = get_object_or_404(Lesson, pk=lesson_id)
            if form.is_valid():
                form.save(Comment, request.user, lesson)

                messages.success(request, "Izoh muvaffaqiyatli qo'shildi.")
                return redirect('lesson_detail', lesson_id=lesson_id)
    else:
        messages.error(request, "Iltimos, tizimga kirishingiz kerak.")
        return redirect('login')


def comment_delete(request: WSGIRequest, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.user == comment.author or request.user.is_superuser:
            lesson_id = comment.lesson.id
            comment.delete()
            messages.success(request, "Izoh muvaffaqiyatli o'chirildi!")
            return redirect('car_detail', lesson_id=lesson_id)


def comment_update(request: WSGIRequest, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_id)
        lesson_id = comment.lesson.id
        if request.user == comment.author or request.user.is_superuser:
            if request.method == 'POST':
                form = CommentForm(data=request.POST)
                if form.is_valid():
                    form.update(comment)

                    messages.success(request, "Izoh muvaffaqiyatli o'zgartirildi.")
                    return redirect('lesson_detail', lesson_id=lesson_id)

            else:
                form = CommentForm(initial={'text': comment.text})

            context = {
                'car': comment.car,
                'form': form,
                'update': True,
                'comment': comment,
                'comments': Comment.objects.filter(lesson_id=lesson_id)
            }

            return render(request, 'lesson.html', context)

    else:
        messages.error(request, "Iltimos, tizimga kirishingiz kerak.")
        return redirect('login')

def update_course(request: WSGIRequest, course_id):
    types = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():

            if Course.objects.filter(name=form.cleaned_data.get('name')).exists():
                messages.success(request, "Ma'lumot o'zgartirilmadi. Bunday ma'lumot allaqachon qo'shilgan.")
                return redirect('home')

            types.name = form.cleaned_data.get('name')
            types.save()

            messages.success(request, "Ma'lumot muvaffaqiyatli o'zgartirildi.")
            return redirect('home')

    forms = CourseForm(initial={
        'name': types.name
    })

    context = {
        'forms': forms,
        'current_year': datetime.now().year
    }

    return render(request, 'addType.html', context)

def delete_course(request, course_id):
    type = get_object_or_404(Course, pk=course_id)
    type.delete()
    messages.success(request, "Ma'lumot muvaffaqiyatli o'chirildi.")
    return redirect('home')

def update_lesson(request: WSGIRequest, lesson_id):
    lesson = get_object_or_404(Course, pk=lesson_id)

    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            lesson.title = form.cleaned_data.get('title')
            lesson.teacher = form.cleaned_data.get('teacher')
            lesson.content = form.cleaned_data.get('content')
            lesson.course = form.cleaned_data.get('title')
            lesson.save()

            messages.success(request, "Ma'lumot muvaffaqiyatli o'zgartirildi.")
            if lesson.published:
                return redirect('lesson_detail', lesson_id=lesson_id)
            else:
                return redirect('home')

    forms = LessonForm(initial={
        'title': lesson.title,
        'teacher':lesson.teacher,
        'content':lesson.content,
        'course':lesson.course
    })

    context = {
        'forms': forms
    }

    return render(request, 'addLesson.html', context)

def delete_lesson(request, lesson_id):
    lesson = get_object_or_404(lesson, pk=lesson_id)
    lesson.delete()

    messages.success(request, "Ma'lumot muvaffaqiyatli o'chirildi.")
    return redirect('home')

def register(request: WSGIRequest):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            User.objects.create_user(username, email, password)

            # Xabarni qo'shish
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'auth/sign_up.html', {'form': form})




def loginPage(request: WSGIRequest):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
                return redirect('home')
            else:
                messages.error(request,
                               "Kiritilgan foydalanuvchi nomi yoki parol noto`g`ri. Iltimos, qayta tekshirib ko`ring.")

    context = {
        'forms': LoginForm(),
        'current_year': datetime.now().year
    }

    return render(request, 'auth/login.html', context)

def logoutPage(request: WSGIRequest):
    logout(request)
    messages.success(request, "Tizimdan muvaffaqiyatli chiqdingiz!")
    return redirect('home')


