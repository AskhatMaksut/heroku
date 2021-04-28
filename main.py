import subprocess
subprocess.call('soffice --headless --convert-to pdf:writer_pdf_Export --outdir /app *.docx')
