# expected output
#
# $ ./variations.py
# Enter a message: This is my message
# Lowercase: this is my message
# Uppercase: THIS IS MY MESSAGE
# Capitalized: This is my message
# Title Case: This Is My Message
# Words: ['This', 'is', 'my', 'message']
# Alphabetic First Word: is
# Alphabetic Last Word: This


# message = input("Enter a message: ")
message = "This is my message"
print(f"Lowercase: {message.lower()}")
print(f"Uppercase: {message.upper()}")
print(f"Capitalized: {message.capitalize()}")
print(f"Title Case: {message.title()}")
print(f"Words: {message.split()}")
sorted_words = sorted(message.split())
print(f"Alphabetic First Word: {sorted_words[0]}")
print(f"Alphabetic Last Word: {sorted_words[-1]}")

