from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from com_in_ai_utils.utils import decodeSound
import speechToText

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index2.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    data = request.get_json()
    sound_data = data['sound']
    decodeSound(sound_data, "audio123.wav")
    result = speechToText.speech2Text("audio123.wav")
    return jsonify({"Result": str(result)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
