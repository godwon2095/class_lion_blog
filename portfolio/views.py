from django.shortcuts import render
from .models import Portfolio

def portfolio_list(request):
    portfolios = Portfolio.objects.all()

    return render(request, 'list.html', {'portfolios': portfolios})