# Importing specific libararies used.
import phonenumbers
from phonenumbers import geocoder, carrier

# Filling in the phone number and creating a 'parse'
phone_num = phonenumbers.parse("+27617867868")

# Creating a carrier and region variable for the number and making the language to be in english
Carrier = carrier.name_for_number(phone_num, 'en')
Region = geocoder.description_for_number(phone_num, 'en')

# printing out the information.
print(f"| country | supplier |\n |=====================================\n{Region} | {Carrier} | {phone_num}")