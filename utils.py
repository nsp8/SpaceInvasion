import os


def get_path(folder, file_name):
    _path = os.path.join(os.getcwd(), folder, file_name)
    if os.path.exists(_path):
        return _path
    return None
