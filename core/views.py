import datetime

from django.core.cache import cache

from .zhengwen import zhengwen_fix
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from .forms import AuthorForm,AfterForm,AbstractForm
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
        abstract_form = AbstractForm(request.POST, request.FILES)
        if  abstract_form.is_valid():
            abstract_form.save()
            dict_second =  cache.get('dict')
            dict_result2 =  add_dict(dict(request.POST), dict_second)
            cache.set('dict',dict_result2)
            cache.set('up_name', request.FILES['wendang'].name)

            print(dict_result2)
            return render(request, "core/after.html", {"after_form": after_form})
        else:
            return  render(request, "core/download.html", )

#基本成功
def download_pdf(request):
    dict_third = cache.get('dict')
    dict_result3 = add_dict(dict(request.POST), dict_third)
    cache.set('dict', dict_result3)
    print(dict_result3)

    name = cache.get('filename')
    up_name = cache.get('up_name')
    zhengwen_fix(up_name)
    print(name)
    final(dict_result3,name,up_name)
    file = open('static/pdfresult/'+name+'.docx', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename =result.docx'
    return response
