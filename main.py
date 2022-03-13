from module.search import search
import sys

def main():
    args = sys.argv[1:]
    if len(args)>1 and args[0] == '--nick':
        nickname = args[1]
        search(nickname)

if __name__ == '__main__':
    main()