import os
import re
from pyunpack import Archive


def mkdir(dir_name):
    if os.path.isdir(dir_name):
        return

    try:
        os.mkdir(dir_name)
    except OSError:
        print("Creation of the directory %s failed" % dir_name)
    else:
        print("Successfully created the directory %s" % dir_name)


def extract_archive(target_file, destination_dir):
    mkdir(destination_dir)

    try:
        Archive(target_file).extractall(destination_dir)
    except ValueError:
        print("Archive \"%s\" not found" % target_file)
    else:
        print("Successfully extracted archive to \"%s\"" % destination_dir)


def list_files_by_extension(target_dir, extension):
    excluded_names = [
        "__MACOSX"
    ]

    paths = []

    for item in os.listdir(target_dir):
        subdir = target_dir + "/" + item

        if item in excluded_names:
            continue
        elif os.path.isdir(subdir):
            paths += list_files_by_extension(subdir, extension)
        elif re.search("/*." + extension + "/", subdir):
            paths.append(subdir)

    return paths
