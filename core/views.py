import datetime

from django.core.cache import cache

from .zhengwen import zhengwen_fix
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from .forms import AuthorForm, AfterForm, AbstractForm
import os
from .makeword import add_dict, final, buildend, buildcover,zhuanhuan,doc2pdf

from reportlab.pdfgen import canvas
from docx2pdf import convert


# Create your views here.


def index(request):
    if request.method == "POST":
        author_form = AuthorForm(request.POST)
        abstract_form = AbstractForm()
        if author_form.is_valid():
            sum_dict = {}
            dict_result1 = add_dict(dict(request.POST), sum_dict)
            cache.set('dict0', dict_result1)
            cache.set('filename', request.POST['outputname'])

            print(dict_result1)

            author_form.save()

            return render(request, 'core/abstract.html', {"abstract_form": abstract_form, })
        else:
            return render(request, 'core/error.html', {'form': author_form})
    else:
        author_form = AuthorForm(request.POST)
        return render(request, "core/index.html", {"form": author_form})


def after(request):
    if request.method == "POST":
        after_form = AfterForm()
        abstract_form = AbstractForm(request.POST, request.FILES)
        if abstract_form.is_valid():
            abstract_form.save()
            dict_second = cache.get('dict0')
            dict_result2 = add_dict(dict(request.POST), dict_second)
            cache.set('dict0', dict_result2)
            cache.set('up_name', request.FILES['wendang'].name)
            buildcover(dict_result2)

            print(dict_result2)
            return render(request, "core/after.html", {"after_form": after_form})
        else:
            return render(request, "core/download.html", )


# 基本成功
def download_pdf(request):
    sumdict = {}
    dict_result3 = add_dict(dict(request.POST), sumdict)
    cache.set('dict1', dict_result3)

    buildend(dict_result3)
    print(dict_result3)
    print('这是dic——result4')

    name = cache.get('filename')
    up_name = cache.get('up_name')
    zhengwen_fix(up_name)  #
    final(up_name)
    doc2pdf(r'E:\newcode\untitled6\static\pdffinal\final.docx',r'E:\newcode\untitled6\static\pdffinal\final.pdf')
    file = open('static/pdffinal/final.pdf', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename =result.pdf'
    return response
