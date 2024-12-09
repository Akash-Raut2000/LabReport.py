from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a simple PDF
file_name = "output.pdf"
pdf = canvas.Canvas(file_name, pagesize=letter)

pdf.drawString(100, 750, "Simple Report")
pdf.drawString(100, 730, "Introduction:")
pdf.drawString(100, 710, "This is a simple lab report.")

pdf.save()
print(f"PDF saved as {file_name}")
