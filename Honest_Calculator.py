memory = 0

def error(msg_error):
    if msg_error == 0:
        msg_text = "Enter an equation"
    elif msg_error == 1:
        msg_text = "Do you even know what numbers are? Stay focused!"
    elif msg_error == 2:
        msg_text = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    elif msg_error == 3:
        msg_text = "Yeah... division by zero. Smart move..."
    elif msg_error == 4:
        msg_text = "Do you want to store the result? (y / n):"
    elif msg_error == 5:
        msg_text = "Do you want to continue calculations? (y / n):"
    return msg_text

operends = ['+', '-', '*', '/']

while True:
    while True:
        print(error(0))
        calc = input().split(" ")
        x, oper, y = calc[0], calc[1], calc[2]
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        try:
            x, y = float(x), float(y)
        except ValueError:
            print(error(1))
        else:
            if oper in operends:
                if oper == "+":
                    result = float(x) + float(y)
                    break
                elif oper == "-":
                    result = float(x) - float(y)
                    break
                elif oper == "*":
                    result = float(x) * float(y)
                    break
                else:
                    if (oper == "/") and (y == 0):
                        print(error(3))
                        continue
                    else:
                        result = float(x) / float(y)
                        break
            else:
                print(error(2))
    print(result)

#memory

    while True:
        print(error(4))
        answer = input()
        if answer == 'y':
            memory = result
            break
        elif answer == 'n':
            break
        else:
            break
    while True:
        print(error(5))
        answer = input()
        if answer == 'y':
            break
        elif answer == 'n':
            exit(0)
