import pywhatkit

print('use the country code before number ')
number = input('mobile number :- ')  # Keep the number as a string
data = input("message: ")
hour = int(input('hour: '))
min = int(input('min: '))

# Send a WhatsApp Message to a Contact at the specified time
pywhatkit.sendwhatmsg(number, data, hour, min)
