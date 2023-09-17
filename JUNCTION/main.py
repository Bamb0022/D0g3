import os

from flask import Flask, request
from removebg import RemoveBg
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400

    # 将文件保存到指定路径
    filename = file.filename
    file.save('photo/'+filename)

    output_path = "process_image/" + filename


    rmbg = RemoveBg("cKiVxy8acVYCTS5idwoH72p4", "error.log")  # 引号内是你获取的API
    rmbg.remove_background_from_img_file("photo/"+filename)  # 图片地址

    os.rename("photo/"+filename+"_no_bg.png", output_path)
    return 'File saved successfully'
if __name__ == '__main__':
    app.run(debug=True)