import os


def get_path(path):
    return (os.path.join(path, f)
            for f in os.listdir(path)
            if 'pcap' in f)