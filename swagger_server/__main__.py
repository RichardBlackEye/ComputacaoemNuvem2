#!/usr/bin/env python3

import connexion

from flask import Flask

from swagger_server import encoder


def main():
    app = Flask(__name__, specification_dir='./swagger/') #connexion.App
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Word Development Indicators'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
