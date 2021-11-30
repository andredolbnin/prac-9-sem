import sys
from io import StringIO, BytesIO
from zipfile import ZipFile

with ZipFile(BytesIO(bytes.fromhex(sys.stdin.read()))) as a:
    print(len([f for f in a.infolist() if not f.is_dir()]), sum([f.file_size for f in a.infolist()]))