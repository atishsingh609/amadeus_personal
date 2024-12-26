class FileManager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = None
    def __enter__(self):
        try:
            self.file = open(self.file_path, self.mode)
            return self.file
        except FileNotFoundError:
            raise FileNotFoundError
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
with FileManager('test11.txt', 'r') as file:
    print(file.read())