from flask import Flask, request, send_file
import sys
from YoutubeDownloader import downloader


application = Flask(__name__)


@application.route("/")
def hello():
    html = ("Hello Sangjin <br>"
            "<a href='/youtube/'>Youtube Download</a>")
    return html


@application.route("/youtube/")
def input_id():
    template = ""
    with open("./YoutubeDownloader/form.html", "r") as t:
        template = t.read()
    return template


@application.route("/youtube/download", methods=['POST'])
def download():
    zipfile_name = downloader.download(request.form['playlistId'])
    return send_file('./'+zipfile_name+'.zip', attachment_filename=zipfile_name+'.zip')
'''
    
    return send_file(name_zipfile,
                     mimetype='application/zip',
                     attachment_filename=name_zipfile,
                     as_attachment=True)
'''


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
