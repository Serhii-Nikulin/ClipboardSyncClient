import clipboard
from loguru import logger

clipboard.copy("abcasdfsaf qw r31qr qw f\n"
               "asdf asdf as "
               "as dfq3et1345 "
               "34t 413"
               " ")  # now the clipboard content will be string "abc"
text = clipboard.paste()  # text will have the content of clipboard
if len(text) > 20:
    logger.critical('Syka blyadliviy text nahuy pidor');