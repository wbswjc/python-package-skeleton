#!python3
import os
import re
from typing import Dict

import package

scripts_dir = package.get_package_info('scripts_dir')

scripts_path = package.resource_path(scripts_dir)


class Command:
    def __init__(self, exec: callable, description: str):
        self.exec = exec
        self.description = description


def print_commands_map(m: Dict[str, Command]):
    """Print commands map"""
    import shutil

    print('Available commands:\n')

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
        print_commands_map(commands_map)

    return Command(help_command, 'List all available commands.')


def get_commands_map() -> Dict[str, Command]:
    """Get all available commands."""
    commands = {}

    scripts_module = __import__(scripts_dir)
    for filename in os.listdir(scripts_path):
        match = re.match('^(.*).py$', filename)
        if match and os.path.isfile(os.path.join(scripts_path, filename)):
            name = match.group(1)
            try:
                __import__('{}.{}'.format(scripts_dir, name))
                module = getattr(scripts_module, name)
                exec = module.main
                description = module.__doc__.replace('\n', '\\n')
                commands[name] = Command(exec, description)
            except Exception as e:
                print('Module "{}.{}" import failed: {}'.format(
                    scripts_dir, name, e))

    return commands


def main(*args) -> None:
    commands_map = get_commands_map()
    help_command = make_help_command(commands_map)
    commands_map['help'] = help_command

    if not args:
        print('What do you want to do?\n')
        print_commands_map(commands_map)
        return

    command_id = args[0]

    # Allow usage like './manage.py scripts/command_id.py'
    match = re.match('{}/(.*)\.py'.format(scripts_dir), command_id)
    if match:
        command_id = match.group(1)

    if command_id not in commands_map:
        print('Command "{}" not exists.\n'.format(command_id))
        print_commands_map(commands_map)
        return

    try:
        commands_map[command_id].exec(package.get_package_info, args[1:])
    except Exception as e:
        if '--debug' in args:
            raise e
        print(e)


if __name__ == '__main__':
    import sys

    main(*sys.argv[1:])
