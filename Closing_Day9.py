class SessionManager:
    def __init__(self):
        self.sessions = {}

    def add_session(self, session_id, status):
        self.sessions[session_id] = status

    def display_sessions(self):
        print(self.sessions)

    def update_session(self, session_id, new_status):
        if session_id in self.sessions:
            self.sessions[session_id] = new_status

    def delete_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]


session = SessionManager()
session.add_session("XYZ", "Active")
session.add_session("ABC", "Inactive")
session.display_sessions()
session.update_session("XYZ", "Closed")
session.delete_session("ABC")
session.display_sessions()