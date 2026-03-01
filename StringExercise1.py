msg = "Welcome to Python 101: Strings"


tyler = msg[-6] + msg[12] + msg[2] + msg[1] + msg[-5]
newMsg = (msg[20] + " " + msg[0:7] + " " + msg[-5:-1] + " " + msg[8:10] + " " + tyler)

print(newMsg.title())
print(newMsg [::-1].title())

