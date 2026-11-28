# -*- coding: utf-8 -*-
import time
from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path

api = KaggleApi()
api.authenticate()

status_obj = api.kernels_status("minhthuy70/mineru")
status = getattr(status_obj, "status", None)
failure = getattr(status_obj, "failure_message", None)

print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Kernel Status: {status}")
if failure:
    print(f"Failure Message: {failure}")
