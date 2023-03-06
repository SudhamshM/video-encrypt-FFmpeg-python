from zipfile import ZipFile
from encrypt import encrypt
import os, sys

def encrypted_zip(new_file_name="") -> str | None:
    """Zip a video to .zip format

    Returns:
        str: Returns the zip filename
    """
    file_name = ''
    if new_file_name is not None:
        file_name = encrypt(new_file_name)
    elif len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        print("No file specified.")
        return None
    # check filename is valid
    if file_name is None:
        return
    print("Adding to result.zip now.")

    # proceed to zip
    with ZipFile('result.zip', 'w') as zip_obj:
        zip_obj.write(file_name)
    # removing old video file since copy exists in zip
    os.remove(file_name)
    return 'result.zip'


def simple_zip(file=""):
    file_name = ''
    new_zip_name = 'result2.zip'
    if file:
        file_name = file
    elif len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        print("No file specified.")
        return None
    with ZipFile(new_zip_name, 'w') as zip_obj:
        zip_obj.write(file_name)


    new_name = 'supplier.bin'
    try:
        os.rename(new_zip_name, new_name)
    except FileExistsError:
        os.remove(new_name)
        os.rename(new_zip_name, new_name)
    finally:
        os.remove(file_name)
        print("Zip file double renamed.")
    
    return new_name

def main():
    if not (zip_name := encrypted_zip()):
        return
    
    # renaming to another extension
    new_name = 'test.bundle'
    try:
        os.rename(zip_name, new_name)
    except FileExistsError:
        os.remove(new_name)
        os.rename(zip_name, new_name)
    finally:
        print("Zip file renamed.")
    simple_zip(new_name)

if __name__ == '__main__':
    main()