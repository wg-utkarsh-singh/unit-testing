from os.path import exists


def read_from_file(file):
    if not exists(file):
        raise Exception("Bad File")
    f = open(file)
    return f.read()
