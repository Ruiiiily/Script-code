import os
from PyPDF2 import PdfFileWriter, PdfFileReader

# 添加水印功能的函数


def create_watermark(input_pdf, output_pdf, watermark):
    # 获取水印
    watermark_obj = PdfFileReader(watermark, strict=False)
    watermark_page = watermark_obj.getPage(0)

    # 创建读取对象和写入对象
    pdf_reader = PdfFileReader(input_pdf, strict=False)
    pdf_writer = PdfFileWriter()

    # 给所有页面添加水印，并新建pdf文件
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    # 筛选pdf物料，并执行添加水印功能的函数
    pdf_file_path = './初始物料'
    pdf_files = os.listdir(pdf_file_path)
    for pdf_file in pdf_files:
        if pdf_file[-3:] == 'pdf':
            input_pdf = pdf_file_path + '/' + pdf_file
            output_pdf = './水印版物料/'+pdf_file[0:-3]+'pdf'
            create_watermark(
                input_pdf=input_pdf, output_pdf=output_pdf, watermark='./水印文件/风变编程水印.pdf')
