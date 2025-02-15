import logging
import os

from config import LOG_DIR


def setup_logging(logger_name: str):
    """Функция устанавливает общие настройки для логгеров"""
    os.makedirs(LOG_DIR, exist_ok=True)
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    log_file_path = os.path.join(LOG_DIR, f'{logger_name}.log')
    file_handler = logging.FileHandler(log_file_path, 'w', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
