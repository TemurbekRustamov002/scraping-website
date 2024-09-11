from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL manzili kiritilmagan'}), 400
    # URL dan ma'lumotlarni to'plash va qaytarish
    return jsonify({'message': 'Ma\'lumotlar to‘plandi', 'url': url})
