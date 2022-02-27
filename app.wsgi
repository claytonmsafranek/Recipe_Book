import sys
sys.path.insert(0, '/var/www/html/hello_flask')

activate_this = '/home/clayton/.local/share/virtualenvs/hello_flask-hSmxkLvB/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file.read(), dict(__file__=activate_this))

from app import app as applicaiton
