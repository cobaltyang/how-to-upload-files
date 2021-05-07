import pythoncom
from docx2pdf import convert
from docxtpl import DocxTemplate, Subdoc
from datetime import datetime
from docx import Document
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os,shutil
import win32com.client as win32
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


def buildcover(context):  #制作封面
    doc = DocxTemplate('static/docx/covermoban.docx')  # 加载模板文件
    doc.render(context) #填充数据
    doc.save('static/pdfresult/head.docx') #保存目标文件


def buildend(content):  #制作后边
    doc = DocxTemplate('static/docx/endmoban.docx')  # 加载模板文件
    print('这里执行了')
    doc.render(content) #填充数据
    doc.save('static/pdfresult/tail.docx') #保存目标文件

def chongmingming(srcpath,dstpath):
    os.rename(srcpath,dstpath)
    print("重命名完毕")

# 多输入实现方式
def final(up_name):

    pythoncom.CoInitialize()
    word = win32.gencache.EnsureDispatch('Word.Application')
    # 非可视化运行
    word.Visible = False
    output = word.Documents.Add()  # 新建合并后空白文档
    # 需要合并的文档路径，这里有个文档1.docx，2.docx，3.docx.
    # files = ['E://newcode//one//3.docx', 'E://newcode//one//2.docx', 'E://newcode//one//1.docx']
    files = ['E://newcode//untitled6//static//pdfresult//tail.docx','E://newcode//untitled6//static//pdfresult//'+up_name, 'E://newcode//untitled6//static//pdfresult//head.docx']
    for file in files:
        output.Application.Selection.Range.InsertFile(file)  # 拼接文

    output.SaveAs('E://newcode//untitled6//static//pdffinal//final.docx')  # 保存
    output.Close()








