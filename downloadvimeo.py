# Salve como download.py e rode: python3 download.py

import yt_dlp

url = ""

ydl_opts = {
    'cookiefile': None,           # None = usa cookies do navegador padrão
    'cookiesfrombrowser': ('chrome',),  # mude para ('safari',) se usar Chrome
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])