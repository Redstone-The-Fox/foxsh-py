#!/usr/bin/env python

# | Imports
import os

# | Functions
...

# | Main Function
def main() -> None:
    while True:
        cmd = input('> ')
        if cmd[:4] == 'echo':
            if cmd[5] == '"' and cmd[-1] == '"' or cmd[5] == '\'' and cmd[-1] == '\'': print(cmd[6:-1])
        elif cmd == 'clear':
            os.system('clear')

# | On Run
if __name__ == '__main__':
    main()