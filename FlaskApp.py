import os
from flask import Flask, jsonify, request, send_from_directory
from numpy import ndarray

# Model-specific imports
from model import model_train, model_predict

app = Flask(__name__)

def convert_numpy_objects(obj):
    if isinstance(obj, dict):
        return {key: convert_numpy_objects(val) for key, val in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_objects(item) for item in obj]
    elif isinstance(obj, ndarray):
        return obj.tolist()
    else:
        return obj


def validate_json(required_keys):
    if not request.is_json:
        return False, jsonify({'error': 'Invalid request format, expected JSON.'})

    missing_keys = [key for key in required_keys if key not in request.json]
    if missing_keys:
        return False, jsonify({'error': f'Missing keys: {", ".join(missing_keys)}'})

    return True, None


@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'API is running'})


@app.route('/train', methods=['POST'])
def train():
    valid, response = validate_json(['type'])
    if not valid:
        return response

    test = request.json.get('type') == 'test'

    print("Training starts ...")
    model_train("Data/cs-train", test=test)
    print("Training completed ...")

    return jsonify({'status': 'Training successful'})


@app.route('/predict', methods=['GET'])
def predict():
    # country = request.args.get('country', 'all')
    # year = request.args.get('year')
    # month = request.args.get('month')
    # day = request.args.get('day')
    # test = request.args.get('type') == 'test'

    country = "all"
    year ="2018"
    month = "2"
    day = "1"
    test = False

    all_countries = ['portugal', 'united_kingdom', 'hong_kong', 'eire', 'spain',
                     'france', 'singapore', 'norway', 'germany', 'netherlands']

    # If 'country' is 'all', use the default list of countries
    if country == 'all':
        countries_to_predict = all_countries
    else:
        countries_to_predict = country.split(',')

    final_result = {}
    for country in countries_to_predict:
        result = model_predict(country, year, month, day, test=test)
        final_result[country] = convert_numpy_objects(result)

    return jsonify(final_result)


@app.route('/logs/<filename>', methods=['GET'])
def get_logs(filename):
    if not filename.endswith(".log"):
        return jsonify({'error': 'Invalid file type. Only .log files are allowed.'}), 400

    log_dir = os.path.join(".", "logs")
    file_path = os.path.join(log_dir, filename)

    if not os.path.isdir(log_dir) or not os.path.exists(file_path):
        return jsonify({'error': 'Log file not found.'}), 404

    return send_from_directory(log_dir, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=8080)
