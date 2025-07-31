import requests
import json

class Bot:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
    
    def get_me(self):
        response = requests.get(f"{self.base_url}/getMe")
        return response.json()
    
    def send_message(self, chat_id, text, reply_markup=None, parse_mode=None):
        data = {
            'chat_id': chat_id,
            'text': text
        }
        
        if reply_markup:
            data['reply_markup'] = json.dumps(reply_markup)
        
        if parse_mode:
            data['parse_mode'] = parse_mode
        
        response = requests.post(f"{self.base_url}/sendMessage", data=data)
        return response.json()
    
    def send_photo(self, chat_id, photo, caption=None):
        data = {
            'chat_id': chat_id,
            'photo': photo
        }
        
        if caption:
            data['caption'] = caption
        
        response = requests.post(f"{self.base_url}/sendPhoto", data=data)
        return response.json()
    
    def answer_callback_query(self, callback_query_id, text=None, show_alert=False):
        data = {
            'callback_query_id': callback_query_id,
            'text': text or '',
            'show_alert': show_alert
        }
        
        response = requests.post(f"{self.base_url}/answerCallbackQuery", data=data)
        return response.json()
    
    def get_updates(self, offset=None, timeout=None):
        data = {}
        
        if offset:
            data['offset'] = offset
        
        if timeout:
            data['timeout'] = timeout
        
        response = requests.get(f"{self.base_url}/getUpdates", params=data)
        return response.json()