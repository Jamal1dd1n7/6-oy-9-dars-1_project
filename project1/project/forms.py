from django import forms

from .models import Course


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

    # course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={
    #     "class": "form-select"
    # }))



