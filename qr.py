import qrcode

# Define the data for the QR code
data = """ Name = Nithushan Mohan
        Id Number = 84932
        """

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image to a file
file_path = "qrcode.png"
qr_image.save(file_path)
print("QR code saved as", file_path)
