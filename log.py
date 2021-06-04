import logging

FORMAT = '%(asctime)s - %(name)s - %(levelname)s at line %(lineno)d in %(filename)s : %(message)s'

logging.basicConfig(filename='mylog.log', filemode='a',level=logging.DEBUG, format=FORMAT)

# logging.info("this is a info message")
# logging.warning("this is warning message")
# logging.error("this is a error message")
# logging.critical("this is crtical message")
