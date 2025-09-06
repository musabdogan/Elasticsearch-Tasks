import requests
import json
import time
from datetime import datetime

# Elasticsearch bağlantı bilgileri
ES_HOST = "http://localhost:9200"
DATA_STREAM = "logs-data"

# Eğer güvenlik açıksa kullanıcı şifre ekle
ES_AUTH = ("elastic", "password")  # Basic Auth
HEADERS = {"Content-Type": "application/json"}

def send_log():
    log_entry = {
        "@timestamp": datetime.utcnow().isoformat() + "Z",
        "level": "INFO",
        "message": "Sample log message",
        "service": "test_service"
    }
    
    url = f"{ES_HOST}/{DATA_STREAM}/_doc"
    response = requests.post(url, headers=HEADERS, auth=ES_AUTH, data=json.dumps(log_entry))
    
    if response.status_code in (200, 201):
        print(f"[{datetime.utcnow()}] Log sent successfully")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    while True:
        send_log()
        time.sleep(10)  # 1 dakika bekle
