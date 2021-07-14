from django import forms


class Feedbacks(forms.Form):
    title = forms.CharField(max_length=50, label='Кратко')
    content = forms.CharField(max_length=5555, label='Подробнее', widget=forms.Textarea)
    author = forms.CharField(max_length=50, label='Автор')


class RequestToCourses(forms.Form):
    name = forms.CharField(max_length=50, label='Ваше имя')
    telegram = forms.CharField(max_length=50, label='Телеграм', required=False)
    phone = forms.CharField(max_length=15, label='Номер телефона')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Логин')
    password = forms.CharField(max_length=50, label='Пароль', widget=forms.PasswordInput)
