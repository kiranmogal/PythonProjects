import phonenumbers
from phonenumbers import timezone, geocoder, carrier

#now we take a phone no. input from any user but the 
#condition is it has to be a string input

number = input("Enter your phone number with country specification code +__ : ")
phone = phonenumbers.parse(number)       #parse / breakdown is to extract general info like country code local code etc from the string input phone no.
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")       #en bcoz wtv phone info it shd be in english
reg = geocoder.description_for_number(phone , "en")

print("General Info :","\n",phone)
print( "Timezone : " , time)
print("Sim Carrier : " , car)
print("Sim Region : " , reg)