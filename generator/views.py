from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def admin(request):
    #             запрос    папка     файл          
      return render(request, 'generator/simple.html') 

def home(request):
    #             запрос    папка     файл    параметр ключ          значение       
    #return render(request, 'generator/home.html', {'password':'hgtfdssjjk%6kbVtddf'})

    return render(request, 'generator/home.html')


def password(request):
    
    # добавляем список всех букв
    characters = list('abcdefghijklmnopqrstuvwxyz')    
    # если галочка ПРОПИСНЫЕ, добавляем в список прописные буквы
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    # если галочка спецзнаки, добавляем в список  спецзнаки       
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    # если галочка цифры, добавляем в список  цыфры           
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))    
    # получем в переменную длину пароля   
    length = int(request.GET.get('length',12))
    # создаем переменную с паролем
    thepassword = ''
    # в цикле добавляем в пароль thepassword случайные знаки из списка  characters   
    for x in range(length):
        thepassword += random.choice(characters)                
        
    # возвращаем пароль
    return render(request, 'generator/password.html', {'password': thepassword})   
       
def about(request):
    #             запрос    папка     файл         
    return render(request, 'generator/about.html')    
    
def simple(request):
    #             запрос    папка     файл          
      return render(request, 'generator/simple.html') 