import os
from pyhrm import create_app

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app()

if __name__ == "__main__":
    app.run()
