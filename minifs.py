
class File:
    def __init__(self, name):
        self.name = name
        self.content = ""

class Folder:
    def __init__(self, name):
        self.name = name
        self.folders = {}
        self.files = {}

class FileSystem:
    def __init__(self):
        self.root = Folder("root")
        self.cwd = self.root
        self.path_stack = []

    def mkdir(self, folder_name):
        if folder_name in self.cwd.folders:
            print("Folder already exists.")
        else:
            self.cwd.folders[folder_name] = Folder(folder_name)

    def touch(self, file_name):
        if file_name in self.cwd.files:
            print("File already exists.")
        else:
            self.cwd.files[file_name] = File(file_name)

    def ls(self):
        print("Folders:", list(self.cwd.folders.keys()))
        print("Files:", list(self.cwd.files.keys()))

    def cd(self, folder_name):
        if folder_name == "..":
            if self.path_stack:
                self.cwd = self.path_stack.pop()
            else:
                print("Already at root.")
        elif folder_name in self.cwd.folders:
            self.path_stack.append(self.cwd)
            self.cwd = self.cwd.folders[folder_name]
        else:
            print("Folder not found.")

    def write(self, file_name, content):
        if file_name in self.cwd.files:
            self.cwd.files[file_name].content = content
        else:
            print("File not found.")

    def cat(self, file_name):
        if file_name in self.cwd.files:
            print(self.cwd.files[file_name].content)
        else:
            print("File not found.")

    def run(self):
        print("Welcome to MiniFS! Type 'help' for commands.")
        while True:
            cmd = input(">> ").strip()
            if not cmd:
                continue
            parts = cmd.split()
            command = parts[0]

            if command == "help":
                print("Commands: mkdir, touch, ls, cd, write, cat, exit")
            elif command == "mkdir" and len(parts) > 1:
                self.mkdir(parts[1])
            elif command == "touch" and len(parts) > 1:
                self.touch(parts[1])
            elif command == "ls":
                self.ls()
            elif command == "cd" and len(parts) > 1:
                self.cd(parts[1])
            elif command == "write" and len(parts) > 2:
                self.write(parts[1], " ".join(parts[2:]))
            elif command == "cat" and len(parts) > 1:
                self.cat(parts[1])
            elif command == "exit":
                print("Exiting MiniFS.")
                break
            else:
                print("Unknown or incomplete command.")

if __name__ == "__main__":
    fs = FileSystem()
    fs.run()
