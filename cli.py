#!/usr/bin/env python3

import argparse
import commands

def multiply(ns):
    """Multiplies all the numbers contained in ns."""
    result = 1
    for n in ns:
        result *= n
    return result

def main():
    """Main entrypoint for the cli."""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    # first command
    add = subparsers.add_parser(commands.ADD)
    add.add_argument("numbers", nargs="+", type=int)

    #second command
    sub = subparsers.add_parser(commands.SUBTRACT)
    sub.add_argument('numbers', nargs='+', type=int)

    #third command
    mul = subparsers.add_parser(commands.MULTIPLY)
    mul.add_argument("numbers", nargs="+", type=int)

    #fourth command
    div = subparsers.add_parser(commands.DIVIDE)
    div.add_argument('numbers', nargs='+', type=int)

    args = parser.parse_args()

    if args.command == commands.ADD:
        result = sum(args.numbers)
        print(f"The sum of {args.numbers} is {result}.")
    elif args.command == commands.SUBTRACT:
        first, *rest = args.numbers
        result = first - sum(rest)
        print(f"The difference of {args.numbers} is {result}.")
    elif args.command == commands.MULTIPLY:
        first, *rest = args.numbers
        result = first * multiply(rest)
        operation = " x ".join(str(i) for i in args.numbers)
        print(f"The result of {operation} is {result}.")
    elif args.command == commands.DIVIDE:
        first, *rest = args.numbers
        result = first / multiply(rest)
        operation = " ÷ ".join(str(i) for i in args.numbers)
        print(f"The result of {operation} is {result}.")
    else:
        parser.print_help()
    
if __name__ == "__main__":
    main()