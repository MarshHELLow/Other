def message(msg_index):
    if msg_index == 0:
        msg_text = "Enter an equation"
    elif msg_index == 1:
        msg_text = "Do you even know what numbers are? Stay focused!"
    elif msg_index == 2:
        msg_text = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    elif msg_index == 3:
        msg_text = "Yeah... division by zero. Smart move..."
    elif msg_index == 4:
        msg_text = "Do you want to store the result? (y / n):"
    elif msg_index == 5:
        msg_text = "Do you want to continue calculations? (y / n):"
    elif msg_index == 6:
        msg_text = " ... lazy"
    elif msg_index == 7:
        msg_text = " ... very lazy"
    elif msg_index == 8:
        msg_text = " ... very, very lazy"
    elif msg_index == 9:
        msg_text = "You are"
    elif msg_index == 10:
        msg_text = "Are you sure? It is only one digit! (y / n)"
    elif msg_index == 11:
        msg_text = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    elif msg_index == 12:
        msg_text = "Last chance! Do you really want to embarrass yourself? (y / n)"

    return msg_text

operation = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y}

def is_one_digit(v):
    return True if -10 < v < 10 and type(v) is int else False

def check(v1, v2, v3):
    msg = ""
    msg += message(6) if is_one_digit(v1) and is_one_digit(v2) else ""
    msg += message(7) if v1 == 1 or v2 == 1 and v3 == "*" else ""
    msg += message(8) if v1 == 0 or v2 == 0 and v3 in ['+', '*', '-'] else ""
    print(message(9) + msg) if msg != "" else ""

def is_int(n):
    return int(n) if float(n).is_integer() else float(n)

def start():
    memory = 0
    while True:
        calc = input(message(0))
        x, oper, y = calc.split()
        try:
            x = memory if x == 'M' else float(x)
            y = memory if y == 'M' else float(y)
            check(is_int(x), is_int(y), oper)
            result = operation[oper](x, y)
            print(float(result))
            if input(message(4)) == 'y':
                if is_one_digit(is_int(result)):
                    msg_index = 10
                    while True:
                        answer = input(globals()[f'msg_{msg_index}'])
                        if answer == 'y':
                            if msg_index < 12:
                                msg_index += 1
                            else:
                                memory = result
                                break
                        elif answer == 'n':
                            break
                else:
                    memory = result
            if input(message(5)) == 'n':
                break
        except ValueError:
            print(message(1))
        except KeyError:
            print(message(2))
        except ZeroDivisionError:
            print(message(3))

if __name__ == '__main__':
    start()
