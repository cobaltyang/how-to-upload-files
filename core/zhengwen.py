from docx import Document
import re
from docx.shared import Cm, Pt, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_LINE_SPACING
from docx.oxml.ns import qn
import re

def zhengwen_fix(filename):
    doc = Document('static/pdfresult/'+filename+'.docx')

    pattern_h1 = r'第\s*[0-9]{1}\s*章'
    pattern_h2 = r"[0-9]{1}\.[0-9]{1}"
    pattern_h3 = r"[0-9]{1}\.[0-9]{1}\.[0-9]{1}"
    pattern_h4 = r"[0-9]{1}\.[0-9]{1}\.[0-9]{1}\.[0-9]{1}"
    for para in doc.paragraphs:

        for run_t in para.runs:
            pipei_h1 = re.search(pattern_h1, run_t.text)
            pipei_h2 = re.search(pattern_h2, run_t.text)
            pipei_h3 = re.search(pattern_h3, run_t.text)
            pipei_h4 = re.search(pattern_h4, run_t.text)
            if pipei_h1:
                run_t.font.name = '黑体'
                run_t.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run_t.font.size = Pt(15)  # 小三号
                print('我是h1')
                print(run_t.text)
                print('我是h1')
            if pipei_h2:
                run_t.font.name = '黑体'
                run_t.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run_t.font.size = Pt(14)  # 四号
                print('我是h2')
                print(run_t.text)
                print('我是h2')
            if pipei_h3:
                run_t.font.name = '黑体'
                run_t.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run_t.font.size = Pt(13)  # 13磅
                print('我是h3')
                print(run_t.text)
                print('我是h3')
            if pipei_h4:
                run_t.font.name = '黑体'
                run_t.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run_t.font.size = Pt(12)  # 小四号
                print('我是h4')
                print(run_t.text)
                print('我是h4')
    doc.save('static/pdfresult/'+filename+'2.docx')
