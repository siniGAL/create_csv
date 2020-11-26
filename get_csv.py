from get_path import get_path
from create_csv import create_csv

path_source = '/Users/macbookpro/Documents/project/dataset/'
path_destination = '/Users/macbookpro/Documents/project/dataset/csv/'

file_path = get_path(path_source)

for file in file_path:
    table = create_csv(file, path_destination)