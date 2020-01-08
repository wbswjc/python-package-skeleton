#!python3
import os
import re
from typing import Dict

import package

commands_dir = package.PackageInfo().get('commands_dir')

scripts_path = package.resource_path(commands_dir)


class Command:
    def __init__(self, func: callable, description: str):
        # a function receives package_info and *args, **kwargs,
        # returns error if occurs
        self.func = func
        self.description = description


def print_commands_map(m: Dict[str, Command]):
    """Print commands map"""
    import shutil

    max_name_length = 5
    for key in m:
        if len(key) > max_name_length:
            max_name_length = len(key)
    name_width = max_name_length + 2

    terminal_width = shutil.get_terminal_size().columns
    if terminal_width < name_width:
        description_width = 100
    else:
        description_width = terminal_width - name_width

    for key in sorted(m):
        description = m[key].description
        print('{}{}'.format(key.ljust(name_width, '.'),
                            description[:description_width]))
        d = description[description_width:]
        gap = ''.join([' ' for _ in range(name_width)])
        while d:
            print('{}{}'.format(gap, d[:description_width]))
            d = d[description_width:]

    print('')


def make_help_command(commands_map: Dict[str, Command]) -> Command:
    """
    Make help command, because it can only be built after the
    commands map was initialized"""

    def help_command(*args, **kwargs):
        print('Available commands:\n')
        print_commands_map(commands_map)

    return Command(help_command, 'List all available commands.')


def get_commands_map() -> Dict[str, Command]:
    """Get all available commands."""
    commands = {}

    scripts_module = __import__(commands_dir)
    for filename in os.listdir(scripts_path):
        match = re.match('^(.*).py$', filename)
        if match and os.path.isfile(os.path.join(scripts_path, filename)):
            name = match.group(1)
            try:
                __import__('{}.{}'.format(commands_dir, name))
                module = getattr(scripts_module, name)
                func = module.main
                description = module.__doc__.replace('\n', '\\n')
                commands[name] = Command(func, description)
            except Exception as e:
                print('Module "{}.{}" import failed: {}'.format(
                    commands_dir, name, e))

    return commands


def main(*args) -> None:
    commands_map = get_commands_map()
    help_command = make_help_command(commands_map)
    commands_map['help'] = help_command

    if not args:
        print('What do you want to do?\n')
        print_commands_map(commands_map)
        return

    command_key = args[0]

    # Allow usage like './manage.py scripts/command_id.py'
    match = re.match('{}/(.*)\.py'.format(commands_dir), command_key)
    if match:
        command_key = match.group(1)

    if command_key in commands_map:
        err = commands_map[command_key].func(package.PackageInfo(), args[1:])
        if err is not None:
            print('Error: {}'.format(err))
        return

    candidates = {}
    for k in commands_map:
        if k.startswith(command_key):
            candidates[k] = commands_map[k]

    if len(candidates) == 0:
        print('Command "{}" not found.\n'.format(command_key))
        print('Available commands:\n')
        print_commands_map(commands_map)
        return

    if len(candidates) == 1:
        for k in candidates:
            err = candidates[k].func(package.PackageInfo(), args[1:])
            if err is not None:
                print('Error: {}'.format(err))
            return

    print('Multiple candidates, can\'t decide:\n')
    print_commands_map(candidates)


if __name__ == '__main__':
    import sys

    main(*sys.argv[1:])
