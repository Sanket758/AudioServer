from flask import Flask, request, redirect, Response, jsonify
from flask_pymongo import PyMongo
from song import Song

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Audio"
mongo = PyMongo(app)

@app.route('/get')
def get():
    pass
 
@app.route('/create', methods=['POST'])
def create():
    reqdata = request.get_json()
    audioFileType = reqdata['audioFileType']
    audioFileMetadata = reqdata['audioFileMetadata']
    # print(audioFileMetadata['ID'])
    if audioFileType == 'song':
        songobject = Song(audioFileMetadata['ID'], audioFileMetadata['Name'],
                            audioFileMetadata['Duration'], audioFileMetadata['Uploadedtime'])
        print(songobject)
    if audioFileType == 'podcast':
        pass
    if audioFileType == 'audiobook':
        pass
    
    return {'success': True}
    
    

@app.route('/delete')
def delete():
    pass

@app.route('/update')
def update():
    pass
     

if __name__ == '__main__':
    app.run()