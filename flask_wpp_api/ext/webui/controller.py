import os
import json
import requests as req

URL_API = os.environ.get('URL_API')

class Session:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    
    def is_session_exists(self, session_id):
        try:
            res = req.get(f"{URL_API}/sessions/find/{session_id}")
            if res.status_code == 200:
                return True
        except:
            pass
        return False
    
    def session_status(self, session_id):
        try:
            res = req.get(f"{URL_API}/sessions/status/{session_id}")
            if res.status_code == 200:
                data = res.json()
                return data['status']
        except:
            pass
        return "Session not found."
    
    def get_all_users(self):
        try:
            res = req.get(f"{URL_API}/sessions/getAll")
            if res.status_code == 200:
                data = res.json()
                return data["data"]
        except:
            pass
        return []
    
    def create_new_session(self, session_id):
        payload = f"id={session_id}&isLegacy=false"
        data = {"username": session_id}
        try:
            res = req.post(
                f"{URL_API}/sessions/add", 
                headers=self.headers, 
                data=payload
            )
            if res.status_code == 200:
                data_res = res.json()
                data["qrcode"] = data_res["data"]["qr"]
            else:
                error_alert = "Session already exists, please use another username."
                data["error"] = error_alert
        except:
            pass
        return data
    
    def delete_session(self, session_id):
        try:
            res = req.delete(
                f"{URL_API}/sessions/delete/{session_id}", 
            )
            if res.status_code == 200:
                data = res.json()
                return data['message']
        except:
            pass
        return "Session not found."


class Chat:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json'
        }
    
    def get_chat_list(self, session_id):
        try:
            res = req.get(f"{URL_API}/chats?id={session_id}")
            if res.status_code == 200:
                data = res.json()
                return data["data"]
        except:
            pass
        return []

    def get_conversation(self, session_id, number_id):
        try:
            res = req.get(f"{URL_API}/chats/{number_id}@s.whatsapp.net?id={session_id}&limit=25")
            if res.status_code == 200:
                data = res.json()
                return data["data"]
        except:
            pass
        return []
    
    def send_text(self, session_id, number_id, text):
        data_res = {}
        try:
            payload = {
                "receiver": f"{number_id}",
                "message": {
                    "text": text
                }
            }
            res = req.post(
                f"{URL_API}/chats/send?id={session_id}", 
                headers=self.headers, 
                data=json.dumps(payload)
            )
            if res.status_code == 200:
                data = res.json()
                data_res['success'] =  data['message']
            else:
                data_res['error'] = "Failed to send the message."
        except:
            data_res['error'] = "Failed to send the message."
        return data_res


class Group:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json'
        }
    
    def get_chat_list(self, session_id):
        try:
            res = req.get(f"{URL_API}/groups?id={session_id}")
            if res.status_code == 200:
                data = res.json()
                return data["data"]
        except:
            pass
        return []

    def get_conversation(self, session_id, group_id):
        try:
            res = req.get(f"{URL_API}/groups/{group_id}@g.us?id={session_id}&limit=25")
            if res.status_code == 200:
                data = res.json()
                return data["data"]
        except:
            pass
        return []
    
    def get_group_metadata(self, session_id, group_id):
        try:
            res = req.get(f"{URL_API}/groups/meta/{group_id}@g.us?id={session_id}")
            if res.status_code == 200:
                data = res.json()
                return data["data"]
        except:
            pass
        return []
    
    def send_text(self, session_id, group_id, text):
        data_res = {}
        try:
            payload = {
                "receiver": f"{group_id}@g.us",
                "message": {
                    "text": text
                }
            }
            res = req.post(
                f"{URL_API}/groups/send?id={session_id}", 
                headers=self.headers, 
                data=json.dumps(payload)
            )
            if res.status_code == 200:
                data = res.json()
                data_res['success'] =  data['message']
            else:
                data_res['error'] = "Failed to send the message."
        except:
            data_res['error'] = "Failed to send the message."
        return data_res