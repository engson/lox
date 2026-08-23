import sys

had_error:bool = False

def main():
    if len(sys.argv) > 2:
        print("Usage: plox [script]")
        sys.exit(64)
    elif len(sys.argv) == 2:
        runFile(sys.argv[1])
    else:
        runPrompt()

def runFile(file: str):
    with open(file) as f:
        print(f.read())
    if had_error:
        sys.exit(65)

def runPrompt():

    pass

def report(line: int, where: str, message: str):
    sys.stderr.write(f"[line {line}] Error {where}: {message}")

def error(line: int, message: str):
    report(line, "", message)

if __name__ == "__main__":
    main()
