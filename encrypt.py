import ffmpeg, secrets, sys, os


def encrypt(video_name=""):
    """Encrypt an mp4 using CENC-AES-CTR scheme.

    Args:
        video_name (str): The video name to encrypt without the extension.
    """
    if len(sys.argv) > 1:
        video_name = sys.argv[1]
    
    if video_name == "":
        print("No file name specified.")
        return
    
    if not os.path.isfile(video_name + ".mp4"):
        print("File doesn't exist, please provide correct path.")
        return
    
    secret_key = secrets.token_hex(16)
    secret_kid = secrets.token_hex(16)
    print("Encrypting...")
    (
        ffmpeg
        .input(video_name + ".mp4")
        .output(encryption_scheme='cenc-aes-ctr',
                encryption_key=secret_key, 
                encryption_kid=secret_kid, 
                filename=video_name + "_enc.mp4", 
                codec='copy', 
                map='0')
        .global_args('-loglevel', 'error')
        .global_args('-y')
        .run()
    )
    with open("result.txt", 'w+') as file:
        file.write(video_name + ".mp4 encrypted with key:kid below.\n")
        file.write(secret_key + ":" + secret_kid)
    print("Written to file.")

if __name__ == '__main__':
    encrypt()