import logging as log

# Level Default Warning
log.basicConfig(level=log.DEBUG, 
                    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s', 
                    datefmt='%Y:%m:%d', 
                    handlers=[
                        log.FileHandler('capa_datos.log'), 
                        log.StreamHandler()
                    ])


if __name__ == '__main__':

    log.debug('Message level debug')
    log.info('Message level info')
    log.warning('Message level warning')
    log.error('Message level error')
    log.critical('Message level critical')
