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
            sys.stdout.write(f"{parts[1]}\n")
            sys.stdout.flush()
            continue
        elif parts[0] == "type":
            if parts[1] in builtins:
                sys.stdout.write(f"{parts[1]} is a shell builtin\n")
            else:
                sys.stdout.write(f"{parts[1]}: not found\n")
            continue

        sys.stderr.write(f"{command}: command not found\n")
        sys.stderr.flush()


if __name__ == "__main__":
    main()
