import datetime

from django.core.cache import cache

from .zhengwen import zhengwen_fix
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from .forms import AuthorForm,ContentForm,AfterForm,AbstractForm
import os
from .makeword import add_dict, final

from reportlab.pdfgen import canvas
from docx2pdf import convert
# Create your views here.



def index(request):
    if request.method == "POST":
        author_form = AuthorForm(request.POST)
        abstract_form = AbstractForm()
        if author_form.is_valid():
            sum_dict = {}
            dict_result1 = add_dict(dict(request.POST),sum_dict)
            cache.set('dict',dict_result1)
            cache.set('filename',request.POST['outputname'])

            print(dict_result1)

            author_form.save()

            return render(request, 'core/abstract.html', {"abstract_form":abstract_form, })
        else:
            return render(request,'core/error.html',{'form':author_form})
    else:
        author_form = AuthorForm(request.POST)
        return render(request, "core/index.html", {"form": author_form})

def after(request):
    if request.method == "POST":
        after_form = AfterForm()
        content_form = ContentForm(request.POST)
        if  content_form.is_valid():
            content_form.save()
            dict_second =  cache.get('dict')
            dict_result2 =  add_dict(dict(request.POST), dict_second)
            cache.set('dict',dict_result2)

            print(dict_result2)
            return render(request, "core/after.html", {"after_form": after_form})
        else:
            return  render(request, "core/download.html", {"abstract_form": content_form})


def download_pdf(request):
    dict_third = cache.get('dict')
    dict_result3 = add_dict(dict(request.POST), dict_third)
    cache.set('dict', dict_result3)
    print(dict_result3)

    name = cache.get('filename')

    print(name)
    final(dict_result3,name)


    file = open('static/pdfresult/'+name+'2.docx', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename =result.docx'
    return response


def abstract(request):
    if request.method == "POST":
        abstract_form = AbstractForm(request.POST)
        content_form = ContentForm()
        if  abstract_form.is_valid():
            abstract_form.save()
            dict_four =  cache.get('dict')
            dict_result4 =  add_dict(dict(request.POST), dict_four)
            cache.set('dict',dict_result4)

            print(dict_result4)
            return render(request, "core/content.html", {"content_form": content_form})
        else:
            return  render(request, "core/download.html", {"abstract_form": content_form})