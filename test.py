import os
import unittest
from PyHackMD import API
base_dir = os.path.dirname(__file__)

class TestAPI(unittest.TestCase):
    def setUp(self):
        # self.temp_dir = os.path.join(base_dir, "temp")
        # if not os.path.isdir(self.temp_dir):
        #     os.mkdir(self.temp_dir)

        with open(os.path.join(base_dir, "token.txt"), "r") as f:
            token = f.read().strip()
        
        self.api = API(token)

    def test_get_me(self):
        data = self.api.get_me()
        for key in ["id", "name", "email", "userPath", "photo", "teams"]:
            self.assertTrue(key in data)

    def test_get_note_list(self):
        data = self.api.get_note_list()
        for key in ["id", "title", "tags", "createdAt", "publishType", "publishedAt", "permalink", "shortId", "lastChangedAt", "lastChangeUser", "userPath", "teamPath", "readPermission", "writePermission"]:
            self.assertTrue(key in data[0])

    def test_note_crud(self): # create, get, update, 
        # create & get
        data = self.api.create_note(title="Test Create Note")
        note_id = data["id"]
        data = self.api.get_note(note_id)
        self.assertTrue(data["content"] == "# Test Create Note")

        # update & get
        self.api.update_note(note_id, content="# Test Update Note")
        data = self.api.get_note(note_id)
        self.assertTrue(data["content"] == "# Test Update Note")

        # delete
        self.api.delete_note(note_id)
        data = self.api.get_note_list()
        self.assertTrue(note_id not in [note["id"] for note in data])

    def test_get_note_read_history(self):
        data = self.api.get_note_read_history()
        for key in ['id', 'title', 'tags', 'createdAt', 'publishType', 'publishedAt', 'permalink', 'shortId', 'lastChangedAt', 'lastChangeUser', 'userPath', 'teamPath', 'readPermission', 'writePermission']:
            self.assertTrue(key in data[0])

if __name__ == "__main__":
    unittest.main()