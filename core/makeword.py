from docx2pdf import convert
from docxtpl import DocxTemplate, Subdoc
from datetime import datetime
from docx import Document
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os,shutil
from .zhengwen import zhengwen_fix

def zhuanhuan(filename):
    c = canvas.Canvas(filename.replace(".docx", ".pdf"))
    c.showPage()
    c.save()
    convert(filename,filename.replace(".docx", ".pdf"))

def timename():
    t = datetime.now().strftime('%H-%M')
    return t

def add_dict(context,sum_dict):
    for key,value in context.items():
        if key == 'csrfmiddlewaretoken':
            continue
        else:
            sum_dict[key] = value[0]

    return sum_dict

def chongmingming(srcpath,dstpath):
    os.rename(srcpath,dstpath)
    print("重命名完毕")

# 多输入实现方式
def final(content,outputname,up_name):
    doc = DocxTemplate('static/docx/moban.docx')  # 加载模板文件
    sd = doc.new_subdoc('static/pdfresult/' + up_name)#用户上传的子文档
    content['mysubdoc'] = sd
    doc.render(content) #填充数据
    doc.save('static/pdfresult/'+outputname+'.docx') #保存目标文件





