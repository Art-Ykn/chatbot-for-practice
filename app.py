

from knowledge_base import knowledge_base
from flask import Flask, request, jsonify, render_template



app = Flask(__name__)

# Функция для поиска ответа в базе знаний
def get_answer(user_message):
    user_message = user_message.lower()  # Приводим к нижнему регистру
    for item in knowledge_base:
        for keyword in item["keywords"]:
            if keyword in user_message:
                return item["answer"]
    return "Извините, я не поняла вопрос. Попробуйте переформулировать или позвоните нам по телефону."

# Маршрут для проверки работы сервера (открывается в браузере)
@app.route('/')
def index():
    return render_template('index.html')

# Маршрут для приёма сообщений от виджета


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Получаем JSON от клиента
    user_message = data.get('message', '')  # Извлекаем сообщение
    answer = get_answer(user_message)  # Ищем ответ
    return jsonify({'answer': answer})  # Отправляем ответ в формате JSON

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)