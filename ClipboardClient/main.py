import clipboard
from loguru import logger

import time

text = clipboard.paste()

while True:
    time.sleep(1)
    new_text = clipboard.paste()
    if text != new_text:
        text = new_text
        logger.debug(text)


