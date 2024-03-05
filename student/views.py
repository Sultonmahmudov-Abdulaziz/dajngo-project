from django.shortcuts import render,get_object_or_404
from .models import Shaharlar, Category, Airveys


# Create your views here.



def index(request):
    shaharlar=Shaharlar.objects.all().order_by('name')
    categories = Category.objects.all()

    data = {
        'shaharlar':shaharlar,
        'categories':categories
    }
    return render(request,template_name= 'student/index.html', context=data)


def category(request,id):
    categories = Category.objects.all()
    category=get_object_or_404(Category, pk=id)
    shaharlar=Shaharlar.objects.filter(category=category)


    data={
        'categories':categories,
        'shaharlar':shaharlar
    }

    return render(request, template_name='student/category.html',context=data)


def airveys(request,id):
    airveyis = Airveys.objects.all()
    airveys=get_object_or_404(Airveys, pk=id)
    shaharlar=Shaharlar.objects.filter(airveys=airveys)
    
    data={
        'airveyis':airveyis,
        'shaharlar':shaharlar,
    }


    return render(request, template_name='student/airveys.html',context=data)