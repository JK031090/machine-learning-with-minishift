import tensorflow as tf
import os.path

import server

if not os.path.exists('mnist.h5'):
    import train

    train.start()

else:
    print('Model exists. Starting server')
    server.start()