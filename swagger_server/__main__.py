#!/usr/bin/env python3

import connexion

from flask import Flask

from swagger_server import encoder

def get_secret(user) -> str:
    return 'You are: {uid}'.format(uid=user)


def main():
    app = connexion.App(__name__, specification_dir='./swagger/') #Flask
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Word Development Indicators'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
