import logging
import requests

class LogglyHandler(logging.Handler):
    def __init__(self, customer_token):
        logging.Handler.__init__(self)
        self.url = f'https://logs-01.loggly.com/inputs/{customer_token}/tag/python'

    def emit(self, record):
        log_entry = self.format(record)
        try:
            requests.post(self.url, data=log_entry, headers={'content-type': 'text/plain'})
        except Exception as e:
            print(f"Failed to send log to Loggly: {e}")

def setup_logger(log_file: str, log_level: int = logging.DEBUG, customer_token: str = None):
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Cria um handler para escrever os logs em arquivo
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)

    # Formatação dos logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Adiciona o handler ao logger
    if not logger.hasHandlers():
        logger.addHandler(file_handler)
    
    # Configura Loggly se o token for fornecido
    if customer_token:
        loggly_handler = LogglyHandler(customer_token)
        loggly_handler.setLevel(log_level)
        loggly_handler.setFormatter(formatter)
        logger.addHandler(loggly_handler)

    return logger
