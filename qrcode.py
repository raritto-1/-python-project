import qrcode
 

data = qrcode.QRCode(
    version=1,  # QR code version (adjust as needed)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border  space around the QR code
)

data.add_data(input("provide the link inside:-"))
data.make(fit=True)

img = data.make_image(fill_color = 'green' , background_color = "black")

f = input("enter the file name ")
da = ".png"
ff = f + da
img.save(ff)