name = "Vardas"
surname = "Pavarde"

print(f"{name.lower()} - {surname.upper()}")

#quote = f"\tHello. \nThis is quote. \nAuthor: {name.lower()} {surname.upper()}"
quote = f""" Hello.
This is quote.
 Author: {name.capitalize()} {surname.capitalize()}"""
print(quote)

b_day_wish = """Cheers to you [NAME], for another trrip around the sun!
Today is about you, [NAME]. I can't wait to celebrate you all day long!
My wish for you, [NAME], is that you get all of your birthday wishes this year!"""

wish = b_day_wish.replace("[NAME]", "Vardas")
print(wish)
