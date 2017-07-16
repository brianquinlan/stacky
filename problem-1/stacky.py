#!/usr/bin/env python3

"""Implements a simple programing language called 'stacky'."""

def interpret(commands):
    """Interpret a sequence of commands for a stack-based programming language.

    Args:
        commands: A list of command to interpret. Each command will be a string.
            The possible commands are:
                '+': Pop the top 2 items on the stack, add them and then push
                     the result on the stack as an integer.
                '-': Pop the top 2 items on the stack. Subtract the top item
                     from the second to top one and push the result on the
                     stack as an integer e.g. a 'commands' of ['10', '3', '-']
                     should result in a stack of [7].
                '*': Pop the top 2 items on the stack, multiple them and then
                     push the result on the stack as an integer.
                <anything else>: Convert the command into an integer and push it
                                 onto the stack.

    Returns:
        The resulting stack after executing the given commands. Examples:
            commands            returns
            ['5', '6', '+']     [11]
            ['5', '6']          [5, 6]
    """

if __name__ == '__main__':
    import sys
    commands = list(l.strip() for l in sys.stdin.readlines() if l.strip())

    stack = interpret(commands)
    for stack_item in reversed(stack):
        print(stack_item)