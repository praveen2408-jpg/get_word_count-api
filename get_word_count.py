from flask_api import FlaskAPI
from flask import request
import json
app = FlaskAPI(__name__)


@app.route('/get_word_count/', methods=['GET', 'POST'])
def get_word_count():
	print(request)
	if request.method == 'GET':
		return 'Invalid Request'

	if request.method == 'POST':
		data =request.get_json()
		output = {}
		if not data:
			output = {'message': 'No Text Received'}
			return output
		for key in data.keys():
			text = data[key]
			text = text.split(' ')
			output[key] = {}
			for word in text:
				if word not in output[key]:
					output[key][word] = 1
				else:
					output[key][word] += 1
		return output

if __name__ == '__main__':
	app.run()

