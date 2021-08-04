import os
import time
from api import app


def setEnv():
    if not os.path.exists('migrations'):
        time.sleep(10) # wait for mysql container to initilize
        os.environ["FLASK_APP"] = "api.py"
        os.system('flask db init')
        os.system('flask db migrate')
        os.system('flask db upgrade')

if __name__ == "__main__":
    setEnv()
    app.run('0.0.0.0')