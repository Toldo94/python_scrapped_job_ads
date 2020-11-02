from django.shortcuts import render
from .data import collect_ads as python_org
from django.core.paginator import Paginator


def index(request):
    return render(request, 'python_org_ads/index.html')


def collect_ads(request):
    addManagr = python_org.collect()

    paginator = Paginator(addManagr.addList, 6)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'addList': page_obj
    }
    return render(request, 'python_org_ads/python_org_ads.html', context)
