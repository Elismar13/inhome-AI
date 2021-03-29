import json

FILE_HEADER = 'temperaturas_internas,temperaturas_externas,umidade,presenca,luminosidade,status_ar,status_porta\n'

class FileController():
    def __init__(self, file_path):
        update = False
        self.file = open(file_path, 'r')
        if(self.file.readline() == ''):
            update = True
        self.file.close()

        self.file = open(file_path, 'a')
        if(update):
            self.file.write(FILE_HEADER)
            self.file.close()

    def write_line(self, line):
        row_line = self.parseLineToCSVRow(line)
        self.file.write(row_line)
        self.file.flush()
        return True

    def parseLineToCSVRow(self, line_dict: dict):
        line = str()

        for key in line_dict.keys():
            line += str(line_dict[key]) + ','
        line += '\n'

        return line