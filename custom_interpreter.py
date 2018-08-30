import code

interpretor = code.InteractiveConsole()

try:
    while True:
        code_string = interpretor.raw_input(">>>")

        interpretor.push(code_string)


except EOFError:  # ^D
    print("\nExit\n")
