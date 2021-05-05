from docx import Document
import re
from docx.shared import Cm, Pt, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_LINE_SPACING
from docx.oxml.ns import qn

def zhengwen_fix(docname):
    docname_correct = 'media/' +  docname
    doc = Document(docname_correct)
    pattern_h1 = r'^(第([0-9]{1})章)'
    pattern_h2= r"^([0-9]{1}).([0-9]{1})"
    pattern_h3 = r"^([0-9]{1}).([0-9]{1}).([0-9]{1})"
    pattern_h4 = r"^([0-9]{1}).([0-9]{1}).([0-9]{1}).([0-9]{1})"
    sum_h1 = sum_h2 = sum_h3 = sum_h4 = 0


    for para in doc.paragraphs:
        if re.match(pattern_h1, para.text) and (len(para.text)<40):
            sum_h1 = sum_h1 + 1         #一级标题
            para.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            para.line_spacing_rule = WD_LINE_SPACING.EXACTLY
            para.paragraph_format.line_spacing = Pt(20)#20磅行距
            para.paragraph_format.space_before = Pt(30)
            para.paragraph_format.space_after = Pt(30)#段前后30磅
            for run in para.runs:
                run.font.name = '黑体'
                run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run.font.size = Pt(15) #小三号

        elif re.match(pattern_h2, para.text) and (len(para.text)<40):    #二级标题
            sum_h2 = sum_h2 + 1
            para.paragraph_format.line_spacing = Pt(20)  # 20磅行距
            para.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT #左对齐；
            para.paragraph_format.space_before = Pt(18)
            para.paragraph_format.space_after = Pt(12)  #段前18磅、段后12磅、
            for run in para.runs:
                run.font.name = '黑体'
                run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run.font.size = Pt(14) # 四号

        elif re.match(pattern_h3, para.text) and (len(para.text) < 40):   #三级标题
            sum_h3 = sum_h3 + 1
            para.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT  # 左对齐；
            para.paragraph_format.line_spacing = Pt(20)  # 20磅行距
            para.paragraph_format.space_before = Pt(12)
            para.paragraph_format.space_after = Pt(12)  # 段前后12磅
            for run in para.runs:
                run.font.name = '黑体'
                run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run.font.size = Pt(13)  # 13磅

        elif re.match(pattern_h4, para.text) and (len(para.text) < 40):  # 四级标题
            sum_h4 = sum_h4 + 1
            para.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT  # 左对齐；
            para.paragraph_format.line_spacing = Pt(20)  # 20磅行距
            para.paragraph_format.space_before = Pt(6)
            para.paragraph_format.space_after = Pt(6)  # 段前后6磅
            for run in para.runs:
                run.font.name = '黑体'
                run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run.font.size = Pt(12)  # 小四号

        else:#正文
            para.paragraph_format.first_line_indent = Inches(0.3) #首行缩进两字符
            para.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY  # 两端对齐；
            para.paragraph_format.line_spacing = Pt(20)  # 20磅行距
            for run in para.runs:
                run.font.name = '黑体'
                run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run.font.size = Pt(12)  # 小四号

    print(sum_h1)
    print(sum_h2)
    print(sum_h3)
    print(sum_h4)
    #设置页边距
    for sect in doc.sections:
        sect.top_margin = Cm(3.2)
        sect.bottom_margin = Cm(2.8)
        sect.right_margin = sect.left_margin = Cm(2.5)
        #页眉页脚高度
        sect.header_distance =Cm(2.2)
        sect.footer_distance =Cm(2.0)
        headsec = sect.header
        headpara =headsec.paragraphs[0]
        headpara.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        head_run = headpara.add_run('石家庄铁道大学毕业设计')
        head_run.font.name = '黑体'
        head_run.element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')  # 设置中文字体


