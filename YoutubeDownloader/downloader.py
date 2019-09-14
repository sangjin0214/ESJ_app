import youtube_dl
import zipfile
import time
import os

#test용 list url : https://www.youtube.com/playlist?list=PLkFt_4WuMCqjnuDqkn1SYvPbimasXNwVn
def download(list_url):
    now = int(time.time())
    savedir = "downloads-" + str(now)
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    options = {'format' : 'bestaudio/best',
               'ignoreerrors' : True,
               'outtmpl' : savedir+'/%(id)s.%(ext)s',
               'postprocessors': [{
                   'key' : 'FFmpegExtractAudio',
                   'preferredcodec' : 'mp3'
               }]
              }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([list_url])
    
    mp3s_zip = zipfile.ZipFile('./'+savedir+'.zip', 'w')

    for filename in os.listdir("./"+savedir):
        mp3s_zip.write("./" + savedir + "/" + filename, compress_type=zipfile.ZIP_DEFLATED)

    mp3s_zip.close()
    
    return savedir