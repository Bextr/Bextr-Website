from os import environ
environ['FREEZING_SITE'] = '1'


from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    # serve the frozen site for testing at http://127.0.0.1:5000
    # freezer.serve()
