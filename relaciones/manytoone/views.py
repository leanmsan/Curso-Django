from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.
def create(request):
    rep = Reporter(first_name = "Leandro", last_name = "Sánchez", email = "leanmsan@gmail.com")
    rep.save()

    art1 = Article(headline = 'Hola Mundo', pub_date = date(2022,4,24), reporter = rep)
    art1.save()
    art2 = Article(headline = 'Holis', pub_date = date(2022,4,20), reporter = rep)
    art2.save()
    art3 = Article(headline = 'Adios', pub_date = date(2022,4,1), reporter = rep)
    art3.save()

    result = art1.reporter.first_name

    res = rep.article_set.count() # type: ignore

    return HttpResponse(res)