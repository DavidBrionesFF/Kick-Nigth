import json
import uuid
import os

class Note:
    def __init__(self, title, content, create_at, no):
        self.title = title
        self.content = content
        self.create_at = create_at
        self.no = no

    @staticmethod
    def create(note):
        file_json = open("data/notes/" + note.get("no") + ".json", "w")
        file_json.write(Note.get_note_format(note))

    def update(self):
        body_note = '{"title":"' + self.title + '", "content": "' + self.content + '", "create_at":"' + str(self.create_at) + '", "no":"' + self.no + '"}'
        file_json = open("data/notes/" + self.no + ".json", "w")
        file_json.write(body_note)

    @staticmethod
    def delete(id):
        dir_note = "data/notes/" + str(id) + ".json"
        os.remove(dir_note)

    @staticmethod
    def get_note_format(note):
        return '{"title":"' + note.get("title") + '", "content": "' + note.get("content") + '", "create_at":"' + str(note.get("create_at")) + '", "no":"' + note.get("no") + '"}'

    @staticmethod
    def find_all():
        notes_json = []
        notes_files = os.listdir("data/notes/")
        
        for file_note in notes_files:
            with open("data/notes/" + file_note) as data_file:
                file_json = json.load(data_file)
                notes_json.append(Note(file_json.get("title"), file_json.get("content"), file_json.get("create_at"), file_json.get("no")))
                data_file.close()
        return notes_json

    @staticmethod
    def generate_no():
        return str(uuid.uuid4()).replace("-","")

    @staticmethod
    def find_by_id(id):
        with open("data/notes/" + str(id) + ".json") as data_file:
            file_json = json.load(data_file)
            return Note(file_json.get("title"), file_json.get("content"), file_json.get("create_at"), file_json.get("no"))