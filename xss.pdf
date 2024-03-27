import sys
if sys.version_info[0] < 3:
    raise SystemExit("Use Python 3 (or higher) only")
import io
import bz2
import base64

def create_malpdf1(filename):
    with open(filename, "w") as file:
        file.write('''%PDF-1.7
        1 0 obj
        <</Pages 1 0 R /OpenAction 2 0 R>>
        2 0 obj
        <</S /JavaScript /JS (app.alert(1))
        >> trailer <</Root 1 0 R>>''')

if __name__ == "__main__":
    print("Creating PDF files..")
    create_malpdf1("test.pdf")
    print("Done!")
