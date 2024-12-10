#Lb2_Встановити python веб фреймворк та запустити веб сервер на порту 8000.
#from flask import Flask

#app = Flask(__name__)

#@app.route("/")
#def hello_world():
#   return "Hello, Flask!"

#if __name__ == "__main__":
#    app.run(port=8000)



#Написати просту обробку запиту метода GET сервером. На запит повертати строку “Hello World!”
#from flask import Flask
#app = Flask(__name__)

#app.route("/", methods=["GET"])  # Обробка GET-запиту
#def hello_world():
#    return "Hello World!"  # Відповідь сервера

#if __name__ == "__main__":
#    app.run(port=8000)


#Написати просту обробку запиту метода GET сервером зі шляхом та параметрами в URL

#from flask import Flask, request
# = Flask(__name__)
#@app.route("/currency", methods=["GET"])
#def get_currency():
    # Отримуємо параметри запиту
#   today = request.args.get('today')  # Параметр today (не використовується, лише як приклад)
#    key = request.args.get('key')  # Параметр key (не використовується, лише як приклад)

    # Повертаємо статичний курс валюти
#    return "USD - 41.5"


#if __name__ == "__main__":
#    app.run(port=8000, debug=True)



#Обробка заголовків запиту. В залежності від значення параметру заголовку “Content-Type”

from flask import Flask, request, jsonify
from xml.etree.ElementTree import Element, tostring

app = Flask(__name__)


@app.route("/content", methods=["GET"])
def handle_headers():
    # Отримуємо заголовок Content-Type
    content_type = request.headers.get('Content-Type')

    # Якщо Content-Type = application/json
    if content_type == "application/json":
        response = {
            "status": "success",
            "message": "This is a JSON response."
        }
        return jsonify(response)

    # Якщо Content-Type = application/xml
    elif content_type == "application/xml":
        root = Element('response')
        status = Element('status')
        status.text = 'success'
        message = Element('message')
        message.text = 'This is an XML response.'
        root.append(status)
        root.append(message)

        # Перетворюємо XML-об'єкт у рядок
        xml_response = tostring(root, encoding='unicode')
        return app.response_class(xml_response, content_type='application/xml')

    # Якщо Content-Type не вказано або невідомий
    else:
        return "This is a plain text response.", 200


if __name__ == "__main__":
    app.run(port=8000, debug=True)



