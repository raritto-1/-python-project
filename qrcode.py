import qrcode

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,  # QR code version (adjust as needed)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border space around the QR code
)

# Input the link
link = input("Enter the link: ")

# Add the data to the QRCode object
qr.add_data(link)
qr.make(fit=True)

# Make the QR code image with specified colors
img = qr.make_image(fill_color='green', back_color='black')

# Input the file name
file_name = input("Enter the file name (without extension): ")

# Save the QR code image as a PNG file
file_path = file_name + ".png"
img.save(file_path)

print("QR code saved as", file_path)
