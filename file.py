import sys, pymupdf, pathlib

filename = sys.argv[1]
with pymupdf.open(filename) as doc:
    text = chr(12).join([page.get_text() for page in doc])
    pathlib.Path(filename + ".txt").write_bytes(text.encode())