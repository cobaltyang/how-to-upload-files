from docx import Document
import re
from docx.shared import Cm, Pt, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_LINE_SPACING
from docx.oxml.ns import qn
import re


def zhengwen_fix(filename):
    doc = Document('media/'+filename)
    pattern_h1 = r'第\s*[0-9]{1}\s*章'
    pattern_h2 = r"[0-9]{1}\.[0-9]{1}"
    pattern_h3 = r"[0-9]{1}\.[0-9]{1}\.[0-9]{1}"
    pattern_h4 = r"[0-9]{1}\.[0-9]{1}\.[0-9]{1}\.[0-9]{1}"
    for para in doc.paragraphs:
        if re.match(pattern_h1, para.text) and (len(para.text) < 40):
            para.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            para.line_spacing_rule = WD_LINE_SPACING.EXACTLY
            para.paragraph_format.line_spacing = Pt(20)  # 20磅行距
            para.paragraph_format.space_before = Pt(30)
            para.paragraph_format.space_after = Pt(30)  # 段前后30磅
            for run in para.runs:
                run.font.name = '黑体'
                run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run.font.size = Pt(15)  # 小三号

        elif re.match(pattern_h2, para.text) and (len(para.text) < 40):  # 二级标题

            para.paragraph_format.line_spacing = Pt(20)  # 20磅行距
            para.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT  # 左对齐；
            para.paragraph_format.space_before = Pt(18)
            para.paragraph_format.space_after = Pt(12)  # 段前18磅、段后12磅、
            for run in para.runs:
                run.font.name = '黑体'
                run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run.font.size = Pt(14)  # 四号

        elif re.match(pattern_h3, para.text) and (len(para.text) < 40):  # 三级标题

            para.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT  # 左对齐；
            para.paragraph_format.line_spacing = Pt(20)  # 20磅行距
            para.paragraph_format.space_before = Pt(12)
            para.paragraph_format.space_after = Pt(12)  # 段前后12磅
            for run in para.runs:
                run.font.name = '黑体'
                run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run.font.size = Pt(13)  # 13磅

        elif re.match(pattern_h4, para.text) and (len(para.text) < 40):  # 四级标题

            para.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT  # 左对齐；
            para.paragraph_format.line_spacing = Pt(20)  # 20磅行距
            para.paragraph_format.space_before = Pt(6)
            para.paragraph_format.space_after = Pt(6)  # 段前后6磅
            for run in para.runs:
                run.font.name = '黑体'
                run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run.font.size = Pt(12)  # 小四号

        else:  # 正文
            para.paragraph_format.first_line_indent = Inches(0.3)  # 首行缩进两字符
            para.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY  # 两端对齐；
            para.paragraph_format.line_spacing = Pt(20)  # 20磅行距
            for run in para.runs:
                run.font.name = '黑体'
                run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')  # 设置中文字体
                run.font.size = Pt(12)  # 小四号
    doc.save('static/pdfresult/' + filename )
