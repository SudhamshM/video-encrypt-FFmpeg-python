from zipfile import ZipFile
from encrypt import encrypt

def encrypted_zip():
    file_name = encrypt("video.mp4")
    # check filename is valid
    if file_name is None:
        return
    print("Adding to result.zip")
    
    # proceed to zip
    with ZipFile('result.zip', 'w') as zip_obj:
        zip_obj.write(file_name)

if __name__ == '__main__':
    encrypted_zip()