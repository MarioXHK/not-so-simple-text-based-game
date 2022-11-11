testlist = ["hi", "hey"]
def testfunction(hello, hey, hi):
    print(hello)
    print(hey)
    print(hi)
print(testlist)
testlist[1] = "hello"
print(testlist)
testfunction("Hello",("Hey","Hi"))