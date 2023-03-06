from zipfile import ZipFile
from encrypt import encrypt

file_name = encrypt("video.mp4")
print("Adding to result.zip")
with ZipFile('result.zip', 'w') as zip_obj:
    zip_obj.write(file_name)