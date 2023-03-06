# Video Encrypt with FFmpeg & Python
A Python program to encrypt an mp4 file using FFmpeg and the cenc-aes-ctr scheme.

Requires FFmpeg to be installed prior to running this program. Get it [from here.](https://ffmpeg.org/download.html)

## Run (2 Methods)
- Through a terminal, `python encrypt.py <filename-without-extension>`
- Through the main method, `encrypt(<filename-without-extension>)`

Information about the key and keyID will be in `result.txt` for decrypting later.
