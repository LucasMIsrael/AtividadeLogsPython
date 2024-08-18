import logging
from logger_config import setup_logger

def main():
    # Substitua 'YOUR_LOGGLY_CUSTOMER_TOKEN' pelo seu token real de entrada do Loggly
    customer_token = '0cacd53e-5330-4e40-941d-b51ff6bdfb08'
    
    # Configura o logger
    logger = setup_logger('app.log', logging.DEBUG, customer_token)

    # Gerando logs em diferentes níveis
    logger.debug('Este é um log de DEBUG: informações detalhadas para diagnóstico.')
    logger.info('Este é um log de INFO: confirmação de que as coisas estão funcionando como esperado.')
    logger.warning('Este é um log de WARNING: algo inesperado aconteceu ou pode acontecer.')
    logger.error('Este é um log de ERROR: o software não conseguiu realizar uma função.')
    logger.critical('Este é um log de CRITICAL: erro grave, o programa pode não continuar.')

if __name__ == '__main__':
    main()
