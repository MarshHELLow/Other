msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

def main():
    operends = ['+', '-', '*', '/']
    print(msg_0)
    calc = input().split()
    try:
        x = float(calc[0])
        y = float(calc[-1])
    except ValueError:
        print(msg_1)
        main()
        return
    else:
        if calc[1] not in operends:
            print(msg_2)
            main()
            return
        return

main()
