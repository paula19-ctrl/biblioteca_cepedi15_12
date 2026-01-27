import time

def timestamp(request):
    return {
        "timestamp": int(time.time())
    }