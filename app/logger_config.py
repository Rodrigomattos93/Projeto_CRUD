from loguru import logger
from sys import stderr

logger.remove()

logger.add(
    sink = stderr,
    level = 'INFO',
    format = "{time} | {level} | {message} | {file}:{line}"    
)