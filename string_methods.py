my_string = "My STRing. a real long string."
print(my_string.lower())
print(my_string.upper())
print(my_string.capitalize())
print(my_string.title())
print("Kevin@example.com" == "kevin@example.com")
print(my_string.isalnum())
print(my_string.isascii())
print("isascii()", "❤".isascii())
print("isupper()", "❤".isupper())
print(".title().istitle()", my_string.title().istitle())
print(".title()", "❤".title())
print(".title().istitle()", "❤".title().istitle())
print(".isdecimal()", "1.0".isdecimal())
print(".isdecimal()", "1222".isdecimal())
print(".isdigit()", "1222".isdigit())
print(".isnumeric()", "3.21".isnumeric())
print(".isalpha()", "1a".isalpha())  # all alpha characters
print(".isalnum()", "1a".isalnum())  # all alphanumeric characters
print(".isidentifier()", "1bear".isidentifier())  # string could be used as a variable name
print(".isidentifier()", "word".isidentifier())  # True
print("this is printable".isprintable())  # True
print("this is printable\n".isprintable())  # False

phrase = "This is a simple phrase"
words = phrase.split()
print(words)
url = "http://www.google.com/foo"
url_parts = url.split('/')
print(url_parts)
last_part = url_parts[-1]
print(last_part)

lines = ['first line', 'line two', 'line 3']
output = '\n'.join(lines)
print(lines)
print(output)

print("Hello my name is {} and I like {}".format("dude", "things"))


