import os
import time

from dotenv import load_dotenv

from nanoleaf import *
from xbox import *

load_dotenv()

nanoleaf_ip = os.getenv("NANOLEAF_IP")
nanoleaf_token = os.getenv("NANOLEAF_TOKEN")

xbox_ip = os.getenv("XBOX_IP")

nanoleaf = Nanoleaf(nanoleaf_ip, nanoleaf_token)

xbox = Xbox(xbox_ip)

last_state = False

while True:
    current_state = xbox.is_on()

    if current_state != last_state:
        if current_state:
            nanoleaf.on()
        else: 
            nanoleaf.off()

        last_state = current_state

    time.sleep(5)