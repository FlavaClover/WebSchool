from django import forms


class Feedbacks(forms.Form):
    title = forms.CharField(max_length=50, label='Кратко')
    content = forms.CharField(max_length=5555, label='Подробнее', widget=forms.Textarea)
    author = forms.CharField(max_length=50, label='Автор')