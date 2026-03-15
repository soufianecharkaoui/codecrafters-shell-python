import sys
import os

builtins = ["echo", "exit", "type"]


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command_line = sys.stdin.readline().strip()

        if not command_line:
            continue

        parts = command_line.split(None, 1)
        command = parts[0]
        args = parts[1] if len(parts) > 1 else ""

        if command_line == "exit":
            break
        elif command == "echo":
            write_output(f"{args}", "info")
            continue
        elif command == "type":
            if args in builtins:
                write_output(f"{args} is a shell builtin", "info")
            else:
                is_executable = False
                for path in os.get_exec_path():
                    if os.access(path, os.F_OK) and any(
                        file == args and os.access(os.path.join(path, args), os.X_OK)
                        for file in os.listdir(path)
                    ):
                        is_executable = True
                        write_output(f"{args} is {os.path.join(path, args)}", "info")
                        break
                write_output(
                    f"{args}: not found", "error"
                ) if not is_executable else None
            continue

        write_output(f"{command_line}: command not found", "error")


def write_output(output, type):
    if type == "info":
        sys.stdout.write(f"{output}\n")
        sys.stdout.flush()
    elif type == "error":
        sys.stderr.write(f"{output}\n")
        sys.stderr.flush()


if __name__ == "__main__":
    main()
