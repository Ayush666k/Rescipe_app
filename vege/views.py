from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import user
from django.contrib messages


def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        print(receipe_name)
        print(receipe_description)
        print(receipe_image)

        Receipe.objects.create(
            receipe_name,
            receipe_description,
            receipe_image
        )
        return redirect('/receipes')
    querySet = Receipe.objects.all()

    if request.GET.get('search'):
        querySet = querySet.filter(receipe_name_icontains = request.GET.get('search'))
    context = {'receipes': querySet}
    return render(request, 'receipes.html', context)


def delete_receipe(request, id):
    querySet = Receipe.objects.get(id = id)
    querySet.delete()

    return redircet('/receipes')
def update_receipe(request, id):
    querySet = Receipe.objects.get(id = id)

    if request.method == "post":
        data=request.POST
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        querySet.receipe_name = receipe_name
        querySet.receipe_description = receipe_description

        if receipe_image:
            querySet.receipe_image =receipe_image

        querySet.save()
        return redirect('/receipes')

    context = {'receipes': querySet}
    return render(request, 'upadate_receipes.html', context)


def login_page(request):
    return render(request, 'login.html')


def register_page(request):
    if request.method == "POST"
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = User.objects.filter(username = username)

    if user.exists():
        messages.info(request, "username already exists")
        return redirect('/register_page/')

    user = User.objects.create(
        first_name = first_name
        last_name = last_name
        username = username

    )

    user.set_password(password)
    user.save()
    messages.info(request, 'Account created successfully!')
    return redirect('/register_page/')


    return render(request, 'register.html')
