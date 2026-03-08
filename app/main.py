import sys

builtins = ["echo", "exit", "type"]


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = sys.stdin.readline().strip()
        parts = command.split(None, 1)
        if not command:
            continue
        elif command == "exit":
            break
        elif parts[0] == "echo":
            write_output(f"{parts[1]}", "info")
            continue
        elif parts[0] == "type":
            if parts[1] in builtins:
                write_output(f"{parts[1]} is a shell builtin", "info")
            else:
                write_output(f"{parts[1]}: not found", "error")
            continue

        write_output(f"{command}: command not found", "error")


def write_output(output, type):
    if type == "info":
        sys.stdout.write(f"{output}\n")
        sys.stdout.flush()
    elif type == "error":
        sys.stderr.write(f"{output}\n")
        sys.stderr.flush()


if __name__ == "__main__":
    main()
