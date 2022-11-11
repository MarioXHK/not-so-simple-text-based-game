import time
texty = "Hello World!"
for i in range(len(texty)):
    print(texty[i], end = "")
    time.sleep(0.05)
time.sleep(2)
texty = "..."
print()
for i in range(len(texty)):
    print(texty[i], end = "")
    time.sleep(0.5)
time.sleep(2)
texty = "Oh thank "
print()
for i in range(len(texty)):
    print(texty[i], end = "")
    time.sleep(0.05)
texty = "HEAVENS!"
for i in range(len(texty)):
    print(texty[i], end = "")
    time.sleep(0.1)
time.sleep(0.5)
texty = " I can"
for i in range(len(texty)):
    print(texty[i], end = "")
    time.sleep(0.05)
print()
texty = "FINALLY"
for i in range(len(texty)):
    print(texty[i], end = "")
    time.sleep(0.1)
texty = " talk like this!"
for i in range(len(texty)):
    print(texty[i], end = "")
    time.sleep(0.05)
time.sleep(1)
print()
texty = "Now sure, I might've google searched one thing\nto try and see how to get string stuff, but\nsurely this is still pretty pogger, right?"
for i in range(len(texty)):
    print(texty[i], end = "")
    if texty[i] == ",":
       time.sleep(0.25) 
    time.sleep(0.05)