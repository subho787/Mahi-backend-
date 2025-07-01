from flask import Flask, request, jsonify
import wikipedia
import requests

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    try:
        answer = wikipedia.summary(question, sentences=2)
        return jsonify({'answer': answer})
    except:
        try:
            url = f"https://api.duckduckgo.com/?q={question}&format=json"
            res = requests.get(url).json()
            if res.get("AbstractText"):
                return jsonify({'answer': res["AbstractText"]})
            else:
                return jsonify({'answer': "Sorry, I couldn't find anything."})
        except:
            return jsonify({'answer': "Something went wrong."})

if __name__ == '__main__':
    app.run(debug=True)