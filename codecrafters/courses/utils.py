import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.lib import colors

def generate_certificate_pdf(certificate):
    """
    Generates a beautiful PDF certificate using ReportLab.
    Returns the raw PDF bytes.
    """
    buffer = io.BytesIO()
    
    # Use landscape letter
    c = canvas.Canvas(buffer, pagesize=landscape(letter))
    width, height = landscape(letter)
    
    # Draw Background Setup
    c.setFillColor(colors.HexColor("#0f172a")) # Dark slate background
    c.rect(0, 0, width, height, fill=1)
    
    # Draw Border
    c.setStrokeColor(colors.HexColor("#0ea5e9")) # Brand primary
    c.setLineWidth(4)
    c.rect(0.5*inch, 0.5*inch, width - 1*inch, height - 1*inch)
    
    c.setStrokeColor(colors.HexColor("#38bdf8")) # Brand secondary
    c.setLineWidth(1)
    c.rect(0.6*inch, 0.6*inch, width - 1.2*inch, height - 1.2*inch)

    # Title
    c.setFont("Helvetica-Bold", 48)
    c.setFillColor(colors.white)
    c.drawCentredString(width / 2.0, height - 2*inch, "Certificate of Completion")
    
    # Subtitle
    c.setFont("Helvetica", 18)
    c.setFillColor(colors.HexColor("#94a3b8")) # slate-400
    c.drawCentredString(width / 2.0, height - 3*inch, "This certificate is proudly presented to")
    
    # User Name
    user_name = certificate.user.get_full_name() or certificate.user.username
    c.setFont("Helvetica-Bold", 36)
    c.setFillColor(colors.HexColor("#38bdf8")) # sky-400
    c.drawCentredString(width / 2.0, height - 4*inch, user_name)
    
    # Context
    c.setFont("Helvetica", 16)
    c.setFillColor(colors.HexColor("#94a3b8"))
    c.drawCentredString(width / 2.0, height - 4.8*inch, "for successfully completing the rigorous curriculum of")
    
    # Course Name
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(colors.white)
    c.drawCentredString(width / 2.0, height - 5.5*inch, certificate.course.title)
    
    # Footer Details
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.HexColor("#64748b")) # slate-500
    
    issue_date = certificate.issue_date.strftime("%B %d, %Y")
    
    # Left align the Certificate ID and Date
    c.drawString(1*inch, 1.2*inch, f"Date: {issue_date}")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, 1*inch, f"ID: {str(certificate.certificate_id)}")
    
    # Generate QR Code for the user's profile (Bottom Right)
    import qrcode
    from django.conf import settings
    # Build complete URL. Assuming local development for now, or using a domain if in prod.
    # To be perfectly safe across environments without request object, we construct a relative path to the profile.
    # In a real deployed app, you'd use a full domain name (e.g., https://codecrafters.com/profile/username)
    profile_url = f"http://127.0.0.1:8000/users/profile/{certificate.user.username}/"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,
    )
    qr.add_data(profile_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code into bytes
    qr_buffer = io.BytesIO()
    img.save(qr_buffer, format="PNG")
    qr_buffer.seek(0)
    
    from reportlab.lib.utils import ImageReader
    qr_image = ImageReader(qr_buffer)
    
    # Draw QR code in the bottom right corner
    qr_size = 1.2 * inch
    c.drawImage(qr_image, width - 1*inch - qr_size, 0.8*inch, width=qr_size, height=qr_size)
    
    c.setFont("Helvetica", 8)
    c.drawRightString(width - 1*inch, 0.6*inch, "Scan to view achievements")
    
    # Finish and convert to bytes
    c.showPage()
    c.save()
    
    buffer.seek(0)
    return buffer.getvalue()
