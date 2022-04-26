""" !!! CESARS CYPHER !!! """

# def button_encode(text, s):
#     entry_3.delete(0, END)
#
#     result = ""
#     for i in range(len(text)):
#         char = text[i]
#         if (char.isupper()):
#             result += chr((ord(char) + s - 65) % 26 + 65)
#             entry_3.insert(0, result)
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
#             entry_3.insert(0, result)
#     return result
#
# def button_decode(text, dec):
#     entry_4.delete(0, END)
#
#     result = ""
#     for i in range(len(text)):
#         char = text[i]
#         if (char.isupper()):
#             result += chr((ord(char) + dec - 65) % 26 + 65)
#             entry_4.insert(0, result)
#         else:
#             result += chr((ord(char) + dec - 97) % 26 + 97)
#             entry_4.insert(0, result)
#     return result