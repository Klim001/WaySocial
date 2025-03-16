from django.shortcuts import render
from .database_functions import *
from .database_functions import PATH
ID = 1

def index(request):

    #id = request.GET.get('id')
    #entry = request.GET.get('entry')
    return render(request, 'main/main.html')


def contacts(requests):
    return render(requests, 'main/contacts.html')


def chat(requests):
    return render(requests, 'main/chat.html')


def settings(requests):
    return render(requests, 'main/settings.html')


def pay(requests):
    return render(requests, 'main/pay.html')


def user_entry(requests):
    global ID
    create_db(PATH)
    add_to_db(PATH, {'id': ID, 'username': 'go', 'password': 'ppp'})
    ID += 1
    name = requests.GET.get('login', '#################################')
    password = requests.GET.get('password', '#################################')

    flag_entry = wright_entry(PATH, str(name), str(password))
    if flag_entry:
        data = {'entry': flag_entry[0]}
        return render(requests, 'main/main_entry.html', data)
    return render(requests, 'main/user.html')

def user_reg(requests):
    name = requests.GET.get('login')
    password = requests.GET.get('password')
    flag = add_to_db(PATH, {'id': ID, 'username': str(name), 'password': str(password)})
    if flag[0]:
        return render(requests, 'main/main_entry.html', {'entry': True})
    return render(requests, 'main/user.html')
