from django import forms
from .models import *
from .validators import user_valid
from django.core.exceptions import ValidationError


class LessonForm(forms.Form):
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        "placeholder": "Nomi",
        "class": "form-control"
    }), label='Nomi')
    teacher = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        "placeholder": "O`qituvchi",
        "class": "form-control"
    }), label='O`qituvchi')
    content = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Matni",
        "class": "form-control"
    }), required=False)
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={
        "class": "form-select"
    }))


class CourseForm(forms.Form):
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        "placeholder": "Nomi",
        "class": "form-control"
    }), label='Nomi')
    teacher = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        "placeholder": "O`qituvchi",
        "class": "form-control"
    }), label='O`qituvchi')
    course_type = forms.CharField(max_length=250,widget=forms.TextInput(attrs={
        "placeholder": "Kurs turi",
        "class": "form-control"
    }), required=False)
    created_at =forms.DateField(widget=forms.DateInput(attrs={
        "placeholder": "Kurs ochilgan vaqt",
        "class": "form-control"
    }))
    student_count = forms.IntegerField(widget=forms.NumberInput(attrs={
        "placeholder": "O`quvchi soni",
        "class": "form-control"
    }))

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Foydalanuvchi nomi",
        validators=[user_valid]
    )

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Elektron pochta manzili"
    )

    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Parol"
    )

    confirm_password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Parolni qayta kiriting"
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Parollar bir-biriga mos kelmayapti. Iltimos, qayta tekshirib, to'g'ri kiriting!")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Foydalanuvchi nomi"
    )

    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': "form-control form-control-lg"
        }),
        label="Parol"
    )


class CommentForm(forms.Form):
    text = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            'placeholder': "Koment uchun joy",
            'class': "form-control",
            'rows': 3,
            'style': 'resize: none;',
        }),
        label="Koment",
    )

    def save(self, comment, user, lesson):
        comment.objects.create(
            text=self.cleaned_data.get('text'),
            author=user,
            lesson=lesson
        )

    def update(self, value):
        value.text = self.cleaned_data.get('text')
        value.save()





