import ffmpeg, secrets, sys, os


def encrypt(video_name="") -> str | None:
    """Encrypt a video to mp4 using the CENC-AES-CTR scheme.

    Args:
        video_name (str): The video name to encrypt without the extension.
    Returns:
        The filename of the encrypted video.
    """

    # check argument and file exists
    if len(sys.argv) > 1:
        video_name = sys.argv[1]
    
    if video_name == "":
        print("No file name specified.")
        return None
    
    if not os.path.isfile(video_name):
        print("File doesn't exist, please provide correct path.")
        return None
    # generate 32-character or 16-byte hex string
    secret_key = secrets.token_hex(16)
    secret_kid = secrets.token_hex(16)
    new_name = video_name.split('.')[0] + "_enc.mp4"

    print("Encrypting.")
    (
        # proceed to ffmpeg encryption
        ffmpeg
        .input(video_name)
        .output(encryption_scheme='cenc-aes-ctr',
                encryption_key=secret_key, 
                encryption_kid=secret_kid, 
                filename=new_name, 
                codec='copy', 
                map='0')
        .global_args('-loglevel', 'error')
        .global_args('-y')
        .run()
    )

    # write result to text file
    with open("result.txt", 'w+') as file:
        file.write(new_name + " encrypted with key:kid below.\n")
        file.write(secret_key + ":" + secret_kid)
    print("Written to file.")
    return new_name

if __name__ == '__main__':
    encrypt()