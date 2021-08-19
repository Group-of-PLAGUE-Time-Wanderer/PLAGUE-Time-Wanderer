#!/users/bin/python
# coding: utf-8


class File:
    def __init__(self, file_path, sep: str = " ", filesize: int = 3015):
        try:
            self.file = open(file_path, "w")
            self.filecontent = self.file.read()
        except IOError:
            print(f"File {file_path} cannot be opened/readen.")
            exit(1)

        self.level = self.filecontent.split(sep, filesize)
