from Ballers import create_app

import os
import sys

sys.path.append(os.path.dirname(__name__))

# create an app instance
app = create_app()

app.run()
