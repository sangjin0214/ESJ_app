from flask import Flask, request, send_file
import sys
from YoutubeDownloader import downloader
from BlankGenerator import testpage, answerpage


application = Flask(__name__)


@application.route("/")
def hello():
    html = ("Welcome to Sangjin's lab <br>"
            "<a href='/youtube/'>Youtube Download</a><br>"
            "<a href='/blankgenerator/'>Blank Generator</a><br>"
            "<a href='/application_confirm/'>Application Confirm</a>"
            "<br><br><br>//update log<br>blankgenerator : level of difficulty added")
    return html


@application.route("/youtube/")
def input_id():
    template = ""
    
    with open("./YoutubeDownloader/form.html", "r") as t:
        template = t.read()
    
    template += "타다닥타다다다닥 제작중; 언젠가 끝나겠지...? 으아아악 에러가... 디버깅디버깅디버깅 흐흑흑 저리가"
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


@application.route("/blankgenerator/")
def textselect():
    template = ""
    with open("./BlankGenerator/form.html", "r") as t:
        template = t.read()
    return template


@application.route("/blankgenerator/blankedtext", methods=['POST'])
def test():
    difficulty = request.form['difficulty']
    title = request.form['title']
    template = testpage.test(difficulty, title)
    return template


@application.route("/blankgenerator/answer", methods=['POST'])
def answer():
    template = answerpage.answer()
    return template

    
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
