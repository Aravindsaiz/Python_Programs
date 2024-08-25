""" this python file starts in cli, takes args for file name. keep on writing to append data to a file"""

import sys
import pathlib

class FileWriterHandler():
    def __init__(self,filename):
        self.filename = filename

    def __enter__(self):
        # print("entered init")
        self.fileobj  = open(pathlib.Path(self.filename),'w')
        return self
    
    def __exit__(self,exec_type,exec_value,exec_trb):
        # print(exec_type,exec_value)
        # print("exiting context handler")
        self.fileobj.close()
    
    def writecontent(self,content):
        self.fileobj.write(content+"\n")




if __name__ == "__main__":
    print(sys.argv)
    filename = sys.argv[1] if len(sys.argv) > 1 else "output.txt"
    with FileWriterHandler(filename) as obj:
        print(obj)
        while True:
            content = input("Enter yout content: ")
            if "exit()" == content:
                break
            else:
                obj.writecontent(content)
