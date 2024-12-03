import firebase_admin
from firebase_admin import credentials, db
import json

cred = credentials.Certificate(json.loads("""
{
  "type": "service_account",
  "project_id": "otto-8275b",
  "private_key_id": "f63557de76643b6a4e7ddaa0951688a7a49611bb",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC5XoY0KDh4i8wl\\ncSIijERbn+LFulo7MkM2eEgpMH2fYAiJMOeBTYUIrwPWWHWhZkX18kauI87TzzmC\\nGjz5xyM7sFVlKEr6KeF1UJjkO9HFA2bW244IubdV/nPP4+7kahd6T6++ROUGw0kb\\nUBgItiMEhLmnqQJA7JGp7nO8Y2zxjWHd/QWvTCb+7/7hVHpeBTOIzbek1XXG78T5\\n8Q1LEnYZswZV0vOHPpIm3hoNF4be9ueHyWe3LZSTjgOU55zwnqAC1A6/msHfgK6q\\nJDC5tMLWkyHZT+tVmiwENPUpXkwMWUoPLVu2t6B1CeDKI858sCiEttdFCRNZ0YQG\\ntgkS0k/PAgMBAAECggEAKMw9DU2s4BskmzkDIkds5B2Uc6BIK68sS9i9SRN7EpC4\\nUDmLOlItbXPXjF17xkIUM8VW+Qy4gLWjGpdbxD2n64MryE/N8LE3BfLvM4xW5t2Q\\nzMkVwaXeS/bs1lx8P5l6AVl4fI/9ODfS50gBgilUG7J6igQQkul+RcBNiLD5UVBE\\nJXBpCaC5bYqYquK5wZdTXbTD/q30VICJ7Bu0PbHc1epqomObFJNlev1ESzy0Krln\\nLWoxQiiEhVYLotTos+rsjQBrN6S/7UODi34kzGQNwyaVmeCwlY6DhzFVLsZv1/Ov\\nRwWmPlSNcS9dy4+j/UbLvp9QeMC4AjrqHynxa/IQAQKBgQD06SOPbFy/jO6dzxr9\\nLTxMQJTLDLfvDZbSv5NRvpT+9377Zhqir/e5Bv+V+8YCT9IaXFYgCX2sAMrBPOqi\\ndcS23+G7ljvyMT5W968yJ/Qg+eDK31IIAjKEfXyPxOqAkPQkDda5PzJOGwQBAhuf\\nZu14HFuTt/q3/Axx73XGKAxVAQKBgQDBwzczEOzLSr72M2OTjDRMbbRHi7pd7ji+\\nUh6vUC4M7q0BMjNR+T0Dv7I6pvQaFILndUItMSJfT7MykVc38empq5cqjXiErTRF\\nimMZXBEZke9hVVGdpFpJ20HnBfe5ViHcaJ3RZLqkLO2c2q12jvd9VrIs1QWKT6lO\\nZdbBdrWUzwKBgEsBR6G6FyGW4NE1x1c4TlowASG6cG5m5AUBJPYI/wqi86G8oHWo\\nnJ5u9UGSzQ6SMY9fLgU7wuA1keLibB17Ida79B8GIK/IwwXRbzdWIx8iR+T5xd6s\\nBZqr78T8ErFzM0IDdvpez2I6RdylL55+4EVDsgwocUF9kLYoFxKr2zMBAoGAG/mJ\\nYLAS4A78nyMwPz9A1cAJBUNhNuqL+r50e69B1tAm3kNXMYCglIf6vYkZOSK4+53s\\nXgX4BnbFUom1Y/hjWgHSI2yld9Jh96BRSnoGZgCx5QWicPYnqv4i963e5D1RSjc4\\ngeDfKZDrBXh1Dub5SHlZ5CslT6DMuurtJKV09fUCgYBcQmqadKonq/nBQ6oTUBQR\\nhOPhLVeAakTreebobr0AqF26if6nykS/4z29srxkV32wdF7nZansSLQA71q/Ghm8\\nv5TOSZoj45+3CcQcUiNfVPKfY+6qc0mY/IGBuvb8qCDH3cdVxS3fRevdGKjR4NyT\\nlkJvM8UqtLrNZ+voNuUtsg==\\n-----END PRIVATE KEY-----\\n",
  "client_email": "firebase-adminsdk-1zc00@otto-8275b.iam.gserviceaccount.com",
  "client_id": "112781614527417813480",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-1zc00%40otto-8275b.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
"""))
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://otto-8275b-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

# Reference to the database
ref = db.reference('/')

# Data to be saved
data = {
    'response': {
        'res': "This is a test OK lr bya san kyi tr?",
        'emotion': "Sad"
    }
}

# Save data to Firebase Realtime Database
def save_data_to_firebase(data):
    ref.set(data)
    print("Data saved successfully!")

save_data_to_firebase(data)

