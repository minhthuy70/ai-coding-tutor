# -*- coding: utf-8 -*-
"""
Wait for Kaggle MinerU Batch 2C Kernel execution to complete.
Polls status every 25 seconds and exits when COMPLETE or FAILED.
Line-buffered for real-time logging.
"""
import time
import sys
from datetime import datetime
from kaggle.api.kaggle_api_extended import KaggleApi

try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass

KERNEL_TARGET = "minhthuy70/mineru-batch-2c-final"

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}", flush=True)

def main():
    log(f"Initializing Kaggle API monitor for {KERNEL_TARGET}...")
    api = KaggleApi()
    api.authenticate()

    start_time = time.time()
    last_status = None
    poll_count = 0

    while True:
        poll_count += 1
        try:
            status_obj = api.kernels_status(KERNEL_TARGET)
            status = getattr(status_obj, "status", None)
            failure = getattr(status_obj, "failure_message", None)
            status_str = str(status)

            elapsed = int(time.time() - start_time)
            elapsed_min = elapsed // 60
            elapsed_sec = elapsed % 60

            if status_str != last_status or poll_count % 3 == 0:
                log(f"Status: {status_str} (Polling #{poll_count}, Elapsed: {elapsed_min}m {elapsed_sec}s)")
                last_status = status_str

            if "COMPLETE" in status_str.upper():
                log(f"🎉 Kaggle Kernel finished successfully! (Total wait time: {elapsed_min}m {elapsed_sec}s)")
                sys.exit(0)
            elif "ERROR" in status_str.upper() or "FAIL" in status_str.upper() or failure:
                log(f"❌ Kaggle Kernel failed: {status_str}")
                if failure:
                    log(f"Failure message: {failure}")
                sys.exit(1)
        except Exception as e:
            log(f"Warning while polling Kaggle status: {e}")

        time.sleep(25)

if __name__ == "__main__":
    main()
