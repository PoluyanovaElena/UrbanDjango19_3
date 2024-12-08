from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
# Create your views here.


def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    games = ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]
    context = {
        'games': games,
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')


def registration_page(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            return HttpResponse(f"Приветствуем, {username}!")
        # return render(request, 'fifth_task/registration_page.html', {'form':form})
        else:
            return render(request, 'fifth_task/registration_page.html', {'form': form})

    else:
        form = UserRegister()
        return render(request, 'fifth_task/registration_page.html', {'form': form})

def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                users.append(username)
                return render(request, 'fifth_task/registration_page.html', {'username': username})
        else:
            info['form'] = form
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            users.append(username)
            return render(request, 'fifth_task/registration_page.html', {'username': username})

    return render(request, 'fifth_task/registration_page.html', info)
