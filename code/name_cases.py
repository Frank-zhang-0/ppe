first_name = "zhang"
last_name = "Frank"
message1 = f"Hello {first_name.title()}, would you like to learn some Python today?"
print(message1)

first_n = f"{first_name.lower()}"
last_n = f"{last_name.lower()}"
message2 = f"{first_n} {last_n}\n{first_name.upper()} {last_name.upper()}\n{first_name.title()} {last_name.title()}"
print(message2)

famous_person = "Alber Einstein"
message3 = f'{famous_person} once said,"A person who never made a mistake never tried anything new."'
print(message3)

name = " Frank zhang "
message4 = f"{name.lstrip()}\n{name.rstrip()}\t{name.strip()}"
print(message4)
