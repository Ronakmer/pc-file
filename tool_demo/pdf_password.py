

a=input('enter passs:')
import pypdf
# Create reader and writer object
reader = pypdf.PdfReader("g.pdf")
writer = pypdf.PdfWriter()
# Add all pages to writer (accepted answer results into blank pages)
for page in reader.pages:
    writer.add_page(page)
# Encrypt with your password
writer.encrypt(f'{a}')
# Write it to an output file. (you can delete unencrypted version now)
with open('encrypted_output.pdf', 'wb') as resultPdf:
    writer.write(resultPdf)




