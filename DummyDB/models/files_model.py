import csv


class FilesModel:
    def create_file(self, name, cols):
        with open(f'{name}.ddb', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(cols)
