#!/usr/bin/env python
import os
import re

from pyunpack import Archive


class Util:
    @staticmethod
    def mkdir(dir_name):
        if os.path.isdir(dir_name):
            return

        try:
            os.mkdir(dir_name)
        except OSError:
            print("Creation of the directory %s failed" % dir_name)
        else:
            print("Successfully created the directory %s " % dir_name)


class ArchiveExtract:
    def __init__(self, target_file, destination_dir):
        Util.mkdir(destination_dir)
        Archive(target_file).extractall(destination_dir)


class GetAllFiles:

    excluded_names = [
        "__MACOSX"
    ]

    @staticmethod
    def by_extension(target_dir, extension):
        paths = []

        for item in os.listdir(target_dir):
            subdir = target_dir + "/" + item

            if item in GetAllFiles.excluded_names:
                continue
            elif os.path.isdir(subdir):
                paths += GetAllFiles.by_extension(subdir, extension)
            elif re.search("/*." + extension + "/", subdir):
                paths.append(subdir)

        return paths


archive = "rsf_pdf.zip"
destination = "unpacked"
ext = "pdf"

ArchiveExtract(archive, destination)

files = GetAllFiles.by_extension(destination, ext)
print('\n'.join(files))
