from __future__ import print_function, absolute_import

import os
import sys
import warnings


def path_to_gamedir(basedir, name):
    """
    Returns the absolute path to the directory containing the game
    scripts an assets. (This becomes config.gamedir.)

    `basedir`
        The base directory (config.basedir)
    `name`
        The basename of the executable, with the extension removed.
    """


    candidates = [ name ]

    game_name = name

    while game_name:
        prefix = game_name[0]
        game_name = game_name[1:]

        if prefix == ' ' or prefix == '_':
            candidates.append(game_name)


    candidates.extend([ 'game', 'data', 'launcher/game' ])

    for i in candidates:

        if i == "renpy":
            continue

        gamedir = os.path.join(basedir, i)

        if os.path.isdir(gamedir):
            break

    else:
        gamedir = basedir

    return gamedir


def path_to_common(renpy_base):
    """
    Returns the absolute path to the Ren'Py common directory.

    `renpy_base`
        The absolute path to the Ren'Py base directory, the directory
        containing this file.
    """

    return renpy_base + "/renpy/common"


def path_to_saves(gamedir, save_directory=None): # type: (str, str|None) -> str
    """
    Given the path to a Ren'Py game directory, and the value of config.
    save_directory, returns absolute path to the directory where save files
    will be placed.

    `gamedir`
        The absolute path to the game directory.

    `save_directory`
        The value of config.save_directory.
    """

    import renpy

    if save_directory is None:
        save_directory = renpy.config.save_directory
        save_directory = renpy.exports.fsencode(save_directory) # type: ignore


    def test_writable(d):
        try:
            fn = os.path.join(d, "test.txt")
            open(fn, "w").close()
            open(fn, "r").close()
            os.unlink(fn)
            return True
        except Exception:
            return False

 
    if renpy.android:
        paths = [
            os.path.join(os.environ["ANDROID_OLD_PUBLIC"], "game/saves"),
            os.path.join(os.environ["ANDROID_PRIVATE"], "saves"),
            os.path.join(os.environ["ANDROID_PUBLIC"], "saves"),
            ]

        for rv in paths:
            if os.path.isdir(rv) and test_writable(rv):
                break
        else:
            rv = paths[-1]

        print("Saving to", rv)
        return rv

    if renpy.ios:
        from pyobjus import autoclass # type: ignore
        from pyobjus.objc_py_types import enum # type: ignore

        NSSearchPathDirectory = enum("NSSearchPathDirectory", NSDocumentDirectory=9)
        NSSearchPathDomainMask = enum("NSSearchPathDomainMask", NSUserDomainMask=1)

        NSFileManager = autoclass('NSFileManager')
        manager = NSFileManager.defaultManager()
        url = manager.URLsForDirectory_inDomains_(
            NSSearchPathDirectory.NSDocumentDirectory,
            NSSearchPathDomainMask.NSUserDomainMask,
            ).lastObject()

        try:
            rv = url.path().UTF8String()
        except Exception:
            rv = url.path.UTF8String()


        if isinstance(rv, bytes):
            rv = rv.decode("utf-8")

        print("Saving to", rv)
        return rv

    if not save_directory:
        return os.path.join(gamedir, "saves")

    if "RENPY_PATH_TO_SAVES" in os.environ:
        return os.environ["RENPY_PATH_TO_SAVES"] + "/" + save_directory

    path = renpy.config.renpy_base

    while True:
        if os.path.isdir(path + "/Ren'Py Data"):
            return path + "/Ren'Py Data/" + save_directory

        newpath = os.path.dirname(path)
        if path == newpath:
            break
        path = newpath

    if renpy.macintosh:
        rv = "~/Library/RenPy/" + save_directory
        return os.path.expanduser(rv)

    elif renpy.windows:
        if 'APPDATA' in os.environ:
            return os.environ['APPDATA'] + "/RenPy/" + save_directory
        else:
            rv = "~/RenPy/" + renpy.config.save_directory # type: ignore
            return os.path.expanduser(rv)

    else:
        rv = "~/.renpy/" + save_directory
        return os.path.expanduser(rv)



def path_to_renpy_base():
    """
    Returns the absolute path to thew Ren'Py base directory.
    """

    renpy_base = os.path.dirname(os.path.abspath(__file__))
    renpy_base = os.path.abspath(renpy_base)

    return renpy_base



android = ("ANDROID_PRIVATE" in os.environ)

def main():

    renpy_base = path_to_renpy_base()

    sys.path.append(renpy_base)


    warnings.simplefilter("ignore", DeprecationWarning)

  
    try:
        import renpy.bootstrap
    except ImportError:
        print("Could not import renpy.bootstrap. Please ensure you decompressed Ren'Py", file=sys.stderr)
        print("correctly, preserving the directory structure.", file=sys.stderr)
        raise


    renpy.__main__ = sys.modules[__name__] # type: ignore

    renpy.bootstrap.bootstrap(renpy_base)


if __name__ == "__main__":
    main()
