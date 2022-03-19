import logging

logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s', level=logging.DEBUG, filename='log.txt')

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
