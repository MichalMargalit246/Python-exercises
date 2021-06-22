from flask import Flask

app = Flask(__name__)

port_number = 3000
if __name__ == '__main__':
    app.run(port=port_number)

