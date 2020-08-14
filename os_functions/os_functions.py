import os


def get_ancestor_dir(directory_path, levels=1):
    ancestor_dir = os.path.abspath(
        os.path.join(
            directory_path, *[os.pardir] * levels))
    return ancestor_dir
