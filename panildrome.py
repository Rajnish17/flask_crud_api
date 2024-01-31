input = "asa"


def check(input):
    reverse=""
    for i in reversed(input):
        reverse += i
    if (input==reverse):
        print("true")
    else: 
        print("false")


check(input)


