import json
from .utils import send_requests

class API():
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": "Bearer " + token}

    def get_me(self):
        url = "https://api.hackmd.io/v1/me"
        res = send_requests("GET", url, headers=self.headers)
        return json.loads(res.text)

    def get_note_list(self):
        url = "https://api.hackmd.io/v1/notes"
        res = send_requests("GET", url, headers=self.headers)
        return json.loads(res.text)

    def get_note(self, note_id):
        assert len(note_id) == 22, "note_id should be with length 22."
        url = "https://api.hackmd.io/v1/notes/" + note_id
        res = send_requests("GET", url, headers=self.headers)
        return json.loads(res.text)

    def create_note(self, title="", content="", read_permission="guest", write_permission="signed_in", comment_permission="everyone"):
        """
        permission: {"owner", "signed_in", "guest"}
        """
        url = "https://api.hackmd.io/v1/notes"
        post_data = {
            "title": title,
            "content": content,
            "readPermission": read_permission,
            "writePermission": write_permission,
            "commentPermission": comment_permission
        }
        res = send_requests("POST", url, headers=self.headers, data=post_data)
        return json.loads(res.text)

    def update_note(self, note_id, content=None, read_permission=None, write_permission=None, comment_permission=None):
        assert len(note_id) == 22, "note_id should be with length 22."
        url = "https://api.hackmd.io/v1/notes/" + note_id
        post_data = {}
        for key, value in [("content", content), ("readPermission", read_permission), ("writePermission", write_permission), ("commentPermission", comment_permission)]:
            if value is not None:
                post_data[key] = value
        res = send_requests("PATCH", url, headers=self.headers, data=post_data)
        return res.text

    def delete_note(self, note_id):
        url = "https://api.hackmd.io/v1/notes/" + note_id
        res = send_requests("DELETE", url, headers=self.headers)
        return res.text

    def get_note_read_history(self):
        url = "https://api.hackmd.io/v1/history"
        res = send_requests("GET", url, headers=self.headers)
        return json.loads(res.text)
