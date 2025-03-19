from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    peoples = [
        {'id': 1, 'name': "raj", 'role' : "backend", 'age': 33 },
        {'id': 2, 'name': "sita", 'role' : "frontend", 'age': 13},
        {'id': 3, 'name': "laxman", 'role' : "backend", 'age': 56},
        {'id': 4, 'name': "bhart", 'role' : "SDL", 'age': 22}
        ]
    for people in peoples:
        print(people)
    return render(request, "index.html", context = {'peoples' : peoples})

def sucess_page(request):
    return HttpResponse("the world is such cruel")

def contact(request):
    return render(request, 'contact.html')

def feedback(request):
    return render(request, 'feedback.html')
