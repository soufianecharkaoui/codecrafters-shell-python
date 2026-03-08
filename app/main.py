import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = sys.stdin.readline().strip()
        if not command:
            continue
        sys.stderr.write(f"{command}: command not found \n")
        sys.stderr.flush()


if __name__ == "__main__":
    main()
