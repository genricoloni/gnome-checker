"""
This script checks the compatibility of gnome-shell extensions with the current gnome-shell version.
It loads the gnome-shell version from the system and the gnome-shell extensions.
Then, it loads the gnome-shell extension version from metadata.json.
Finally, it checks the compatibility of gnome-shell extensions with the current gnome-shell version.
"""

import os
import json
import sys

def load_gnome_version():
    """
    Load gnome-shell version from the system.
    """
    try:
        return os.popen('gnome-shell --version').read().split()[-1].split('.')[0]

    except FileNotFoundError:
        return None

def load_gnome_shell_extensions():
    """
    Load gnome-shell extensions from well-known path.
    """
    path_to_extensions = os.path.expanduser('~/.local/share/gnome-shell/extensions')
    try:
        return os.listdir(path_to_extensions)

    except FileNotFoundError:
        return None


def load_extension_version(extension):
    """
    Load gnome-shell extension version from metadata.json.
    """
    try:
        extension_path = os.path.expanduser('~/.local/share/gnome-shell/extensions/' + extension)
        with open(extension_path + '/metadata.json', 'r', encoding='utf-8') as file:
        #open metadata.json as dictionary
            metadata = json.load(file)
            return metadata['shell-version']

    except FileNotFoundError:
        return None

def check_compatibility(gnome_version):
    """
    Check gnome-shell extensions compatibility with the current gnome-shell version.
    """
    extensions = load_gnome_shell_extensions()
    incompatible_extensions = []
    if not gnome_version or not extensions:
        return None

    for extension in extensions:
        extension_version = load_extension_version(extension)
        if gnome_version not in extension_version:
            incompatible_extensions.append(extension)

    return incompatible_extensions

def main():
    """
    Main function.
    """
    version = sys.argv[1] if len(sys.argv) == 2 else load_gnome_version()
    incompatible_extensions = check_compatibility(version)

    print('Gnome version:', version)
    if not incompatible_extensions:
        print('No incompatible extensions found.')
    else:
        print('Incompatible extensions:')
        for extension in incompatible_extensions:
            #print extension in red color
            print('\033[91m', extension, '\033[0m')

if __name__ == '__main__':
    if not os.popen('gnome-shell --version').read():
        print('Usage:')
        print(' python3 gnome-check.py [version]')
        print('or')
        print(' gnome-checker')
        print("if installed")
        sys.exit()

    if len(sys.argv) > 2:
        print('Usage:')
        print(' python3 gnome-check.py [version]')
        print('or')
        print(' gnome-checker')
        print("if installed")
        sys.exit()


    main()
