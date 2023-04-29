from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect


def header(request):
    context = {
        'menu_item1': 'نخل',
        'menu_item2': 'محصولات',
        'menu_item4': 'ارتباط با ما',
        'menu_item5': 'ورود',
        'menu_item6': 'ثبت نام',
        'menu_item7': 'خروج',

    }
    return render(request, 'base/header.html', context)


def footer(request):


    context = {


    }
    return render(request, 'base/footer.html', context)

def home_page(request):
    context = {

    }
    return render(request, 'home_page.html', context)



from django.template import RequestContext

