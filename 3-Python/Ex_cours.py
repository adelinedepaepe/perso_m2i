message = "\n\t\t\n    Ceci est un message avec des espaces au début et à la fin.\n\n   \t"

message = message.lstrip().rstrip()

print(message)

print (len(message))

print(message.capitalize())
print(message.count("un"))
