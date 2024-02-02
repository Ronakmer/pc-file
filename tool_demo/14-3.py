from PIL import Image
# Adding the GUI interface
from tkinter import *
import os


from PIL import Image
# To convert the image From JPG to PNG : {Syntax}
# img = Image.open("person.jpg")
# img.save("Image.png")


# file='person.png'
# file='hi.jpg'

# img = Image.open(f'{file}')
# print(img,'000000000000000000000000')
# img.save(f'{file}')
# # To convert the Image From PNG to JPG
# img = Image.open("Image.png")
# img.save("1.jpg")





# from PIL import Image

# foo = Image.open(f'{file}')  # My image is a 200x374 jpeg that is 102kb large
# foo.size  # (200, 374)

# # downsize the image with an ANTIALIAS filter (gives the highest quality)
# foo = foo.resize((150,150),Image.ANTIALIAS)

# foo.save(f'{file}', quality=95)  # The saved downsized image size is 24.8kb

# foo.save(f'{file}', optimize=True, quality=95)  # The saved downsized image size is 22.9kb



# Import Libraries
# from pdf2docx import parse
# from typing import Tuple
import PyPDF2
from pdf2docx import Converter

# FILE_PATH = '34DPJ142.pdf'
# docx_file = 'sample.docx'


# cv = Converter(FILE_PATH)
# cv.convert(docx_file)
# cv.close()


a='a.jpg'

# image_1 = Image.open(f'{a}')
# im_1 = image_1.convert('RGB')
# im_1.save(f'{a}.pdf')

# result = os.path.splitext(f'{a}')[0]
# print(result,'00000000000000000000')
# im1 = Image.open(a)
# print(im1,'11111111111111111111111')
# im1.save(a)


# logo = Image.open(a)
# print(logo,'000000000000000000000')
# logo.save(a,format='ICO',sizes=[(40, 40)])
# print(logo,'1111111111111111111111')




# filename = r'logo.png'
# img = Image.open(filename)
# img.save('logo.ico')




# logo = Image.open("C:\\Users\\sai mohan pula\
# molu\\Desktop\\geeks_dir\\gfgLogo.png")
 
# logo.save("C:\\Users\\sai mohan pulamolu\\Des\
# ktop\\geeks_dir\\gfgLogoIco_40.ico", format='ICO',
#           sizes=[(40, 40)])




# result = os.path.splitext(f'{file}')[0]

# # logo = Image.open(f"{logUser.img}")
# # print(logo,'222222222222222222222')
# result= result + '.ico'
# print(result,'0000000000')

# a='a.jpg'

# logo = Image.open(f"{a}")

# logo.save(f"{a}",format='ICO')






from pdf2docx import Converter

pdf_file = '34DPJ142.pdf'
docx_file = 'df.docx'


# try:
#     # Converting PDF to Docx
#     cv_obj = Converter(pdf_file)
#     cv_obj.convert(docx_file)
#     cv_obj.close()

# except:
#     print('Conversion Failed')
    
# else:
#     print('File Converted Successfully')


import os
from docx2pdf import convert

from pdf_compressor import Compress
 
ee='demo.docx'
aa='ro.pdf'
# Compress(pdf_file,ee)
# convert(ee)
# convert(ee, aa)
ao='demo.ico'
file='aa.png'

import imageio
import imageio.v2 as imageio


# img = imageio.imread(file)
# imageio.imwrite(ao, img)

###########################################################################

# from PIL import Image
# filename = r'demo.png'
# img = Image.open(filename)
# img.save('logo.ico')

###########################################################################


# import aspose.slides as slides

# # Instantiate an object that represents a PPT file
# presentation = slides.Presentation("samplepptx.pptx")

# # Save the PPT file as PDF
# presentation.save("file.pdf", slides.export.SaveFormat.PDF)




# shutil.make_archive(folderName, 'zip', folderName)







# import pandas as pd


# # Reading the csv file
# df_new = pd.read_csv('demo.csv')

# # saving xlsx file
# GFG = pd.ExcelWriter('Names.xlsx')
# df_new.to_excel(GFG, index=False)

# GFG.save()




# # Importing Required Modules
# from rembg import remove
# from PIL import Image

# # Store path of the image in the variable input_path
# input_path = 'rd.png'

# # Store path of the output image in the variable output_path
# output_path = 'demo.png'

# input = Image.open(input_path)

# output = remove(input)

# #Saving the image in the given path
# output.save(output_path)




# import tabula
# df = tabula.read_pdf("IPLmatch.pdf", pages='all')[0]
# tabula.convert_into("IPLmatch.pdf", "iplmatch.csv", output_format="csv", pages='all')
# print(df)


import imageio

# a='rd.png'
# b='demo.ico'
# img = imageio.imread(a)
# imageio.imwrite(b, img)

import textwrap
from fpdf import FPDF
from PIL import Image
#################
from pypdf import PdfReader,PdfWriter

# reader=PdfReader('g.pdf')
# writer=PdfWriter()

# for page in reader.pages:
#     page.compress_content_streams()
#     writer.add_page(page)

# with open("out.pdf","wb") as f:
#     writer.write(f)


import subprocess
# li=subprocess.run(['hi.pptx','s.pdf -o res.pptx'])

import pandas as pd

# a='Names.xlsx'
# b='name.csv'

# read_file = pd.read_excel ('Names.xlsx')
# read_file.to_csv ('name.csv', index = None, header=True)

# df = pd.DataFrame(pd.read_csv('name.csv'))
  
# df



# import aspose.slides as slides
# with slides.Presentation() as pres:

#     pres.slides.remove_at(0)

#     pres.slides.add_from_pdf("g.pdf")

#     pres.save("file.pptx", slides.export.SaveFormat.PPTX)


from PIL import Image, ImageDraw, ImageFont #dynamic import

# gif='deoeo.gif'
# img = Image.open(gif)
# img.save(gif+".png",'png', optimize=True, quality=70)


# img = Image.open('C:/Python27/image.bmp')
# new_img = img.resize( (256, 256) )
# new_img.save( 'C:/Python27/image.png', 'png')



# logo = Image.open("C:\\Users\\sai mohan \
# pulamolu\\Desktop\\geeks_dir\\gfgLogo.png")
 
# logo.save("C:\\Users\\sai mohan pulamolu\\D\
# esktop\\geeks_dir\\gfgLogoIco.ico",format='ICO')


import imageio

import imageio.v3 as iio


# img = iio.imread('demo.png')
# iio.imwrite('demo.ico', img)




import pandas as pd
import pdfkit

# df = pd.read_excel("Names.xlsx")
# df.to_html("file.html")
# pdfkit.from_file("file.html", "file.pdf")


import subprocess

# path = '[demo.mp4]'

# subprocess.run('ffmpeg -i "demo.mp4".mp4 "de".mp3',shell=True)

import shutil,os


folderName='out.pdf'
a='g'
# shutil.make_archive(a, 'zip', folderName)


from zipfile import ZipFile
import shutil 
import os.path

# Creating the ZIP file 
# archived = shutil.make_archive(a, 'zip', folderName)

from zipfile import ZipFile

# textFile = ZipFile("a.zip", "w")
# textFile.write(folderName)
# textFile.close()


import subprocess
import shutil

# input_filename = 'demo.docx'
# output_filename = 'output.pdf'

# p = subprocess.Popen(['unoconv', '--stdout', input_filename], stdout=subprocess.PIPE)
# with open(output_filename, 'wb') as output:
#    shutil.copyfileobj(p.stdout, output)







import os
import shutil

# src = "demo.pptx"
# dst = "ron.pdf"
# ext = ['ppt', 'pptx', 'doc', 'docx']

# for root, subfolders, filenames in os.walk(src):
#     for filename in filenames:
#         if os.path.splitext(filename)[1] in ext:
#             shutil.copy2(os.path.join(root, filename), os.path.join(dst, filename))            
        
# def ConvertToPDF(ext):
#     print('hi')
#     #some code#

# ConvertToPDF('.ppt')
# ConvertToPDF('.pptx')
# ConvertToPDF('.doc')
# ConvertToPDF('.docx')


from PIL import Image

# logo = Image.open("aa.png")

# logo.save("f.ico",format='ICO',sizes=[(40, 40)])

# import imageio

# img = imageio.imread('aa.png')
# imageio.imwrite('logo.ico', img)





import subprocess

# path = '[demo.webm]'

# subprocess.run('ffmpeg -i "demo".m4v "filename".mp4',shell=True)



# import comtypes.client



# def PPTtoPDF(inputFileName, outputFileName, formatType = 32):
#     inputFileName='demo.pptx'
#     powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
#     powerpoint.Visible = 1

#     if outputFileName[-3:] != 'pdf':
#         outputFileName = outputFileName + ".pdf"
#     deck = powerpoint.Presentations.Open(inputFileName)
#     deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
#     deck.Close()
#     powerpoint.Quit()



from moviepy.editor import VideoFileClip

# videoClip = VideoFileClip("demo.m4v")

# videoClip.write_gif("my-life.gif")




import imageio
# images = []
# filenames=['rd.png']
# for filename in filenames:
#     images.append(imageio.imread(filename))
# imageio.mimsave('movie.gif', images,duration=1,)

# subprocess.run('ffmpeg -i "demo".m4v "filename".mp4',shell=True)

# a= subprocess.run([ 'pdf2pptx -i "34DPJ142".pdf -o "re".pptx' ])
a='34DPJ142.pdf'
b='re.xlsx'
# p = subprocess.Popen(['unoconv', '--stdout', f'{a}'], stdout=subprocess.PIPE)
# with open(fileName, 'wb') as output:
#     shutil.copyfileobj(p.stdout, output)
import pandas as pd

# data= subprocess.run(["pdf2xlsx",a,"-o" ,b ])
a='example.ai'


# resultData = Converter(f'media/{pdfData.uploads}')
# resultData.convert(fileName)
# resultData.close()






# import os
# from pyhtml2pdf import converter

# path = os.path.abspath('1.html')
# converter.convert(f'{path}', 'sample.pdf')





import PyPDF2
import openpyxl
import camelot

import tabula
from tabula.io import read_pdf

i='34DPJ142.pdf'
o='l.csv'

# df=tabula.read_pdf(input_path=i,pages='all')
# tabula.convert_into(input_path=i,output_path=o,output_format="csv",pages='all',stream=True)




# Import the required Module
import tabula
# # Read a PDF File
# df = tabula.read_pdf(i, pages='all')[0]
# # convert PDF into CSV
# tabula.convert_into(i, o, output_format="csv", pages='all')
# print(df)

