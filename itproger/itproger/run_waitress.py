from waitress import serve
from itproger.wsgi import application  # Импортируйте WSGI-приложение Django

if __name__ == '__main__':
    # Запуск сервера Waitress
    serve(application, host='0.0.0.0', port=8000)
