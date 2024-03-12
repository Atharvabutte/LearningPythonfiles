import requests
from tqdm import tqdm


url = ""
r = requests.get(url, stream=True)
totalBytes = int(r.headers["Content-Length"])
bytesReceievd = 0
progress_bar = tqdm(total=totalBytes,unit= "ib",unit_scale=True)
with open("text.exe","wb") as f:
    for chunk in r.iter_content(chunk_size=128):
        progress_bar.update(128)
        f.write(chunk)
        bytesReceievd += 128
progress_bar.close()