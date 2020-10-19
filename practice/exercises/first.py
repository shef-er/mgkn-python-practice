#!/usr/bin/env python
from practice.utils import extract_archive, list_files_by_extension


def run(archive, destination, ext):

    extract_archive(archive, destination)

    files = list_files_by_extension(destination, ext)

    print("Extracted files:\n")
    print('\n'.join(files))
