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
    
    secret_key = "\"" + secrets.token_hex(16) + "\""
    secret_kid = "\"" + secrets.token_hex(16) + "\""
    print(secret_key, secret_kid, sep=':')
    (
        ffmpeg
        .input(video_name + ".mp4")
        .output(video_name + "_enc.mp4", codec='copy')
        .global_args('-y')
        .global_args('-encryption_scheme', 'cenc-aes-ctr')
        .global_args('-encryption_key',  + secret_key)
        .global_args('-encryption_kid', secret_kid)
        .global_args('-report')
        .run()
    )

if __name__ == '__main__':
    encrypt()