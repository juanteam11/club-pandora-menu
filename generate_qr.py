#!/usr/bin/env python3
"""
QR Code Generator for Club Pandora Menu
Generates a QR code that links to the drinks menu.
"""

import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
import sys

def generate_qr_code(url, output_path="club_pandora_qr.png"):
    """
    Generate a QR code with Club Pandora branding
    
    Args:
        url (str): The URL to encode in the QR code
        output_path (str): Path where to save the QR code image
    """
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    # Add data to QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Create a larger image with branding
    img_size = 600
    branded_img = Image.new('RGB', (img_size, img_size + 100), 'white')
    
    # Paste QR code in center
    qr_size = 400
    qr_img = qr_img.resize((qr_size, qr_size))
    qr_position = ((img_size - qr_size) // 2, 50)
    branded_img.paste(qr_img, qr_position)
    
    # Add text
    draw = ImageDraw.Draw(branded_img)
    
    try:
        # Try to use a nice font
        title_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 36)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 24)
    except:
        # Fallback to default font
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # Add title
    title_text = "CLUB PANDORA"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (img_size - title_width) // 2
    draw.text((title_x, 10), title_text, fill="black", font=title_font)
    
    # Add subtitle
    subtitle_text = "Escanea para ver nuestro menú"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (img_size - subtitle_width) // 2
    draw.text((subtitle_x, img_size + 60), subtitle_text, fill="gray", font=subtitle_font)
    
    # Save the image
    branded_img.save(output_path, 'PNG', quality=95)
    print(f"✅ QR code saved as: {output_path}")
    return output_path

def main():
    """Main function to generate QR code"""
    
    # Default URL (you can change this)
    default_url = "file://" + os.path.abspath("index.html")
    
    print("🎭 Club Pandora - Generador de Código QR")
    print("=" * 50)
    
    # Get URL from user or use default
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url_input = input(f"Ingresa la URL del menú (Enter para usar local): ").strip()
        url = url_input if url_input else default_url
    
    print(f"📱 Generando QR para: {url}")
    
    # Generate QR code
    try:
        output_file = generate_qr_code(url)
        print(f"🎉 ¡Listo! Código QR generado exitosamente.")
        print(f"📁 Archivo guardado en: {os.path.abspath(output_file)}")
        print("\n📋 Instrucciones:")
        print("1. Abre el archivo de imagen generado")
        print("2. Imprime el código QR")
        print("3. Colócalo en las mesas del club")
        print("4. Los clientes pueden escanear para ver el menú")
        
    except ImportError:
        print("❌ Error: Faltan librerías necesarias.")
        print("Instala las dependencias con:")
        print("pip install qrcode[pil] pillow")
    except Exception as e:
        print(f"❌ Error al generar QR code: {e}")

if __name__ == "__main__":
    main()
