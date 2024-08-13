import logging

def setup_logger(log_file: str, log_level: int = logging.DEBUG):
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

    return logger
