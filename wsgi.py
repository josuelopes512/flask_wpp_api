from flask_wpp_api import create_app_wsgi

# from threading import Thread
# import os
# from time import sleep
# Thread(target=os.system, args=("startwpp.bat",)).start()
# sleep(1)
app = application = create_app_wsgi()  # noqa
