class DatabaseHandler:
    def __init__(self):
        self.connections = {}

    def add_connection(self, conn_id, status):
        self.connections[conn_id] = status

    def display_connections(self):
        print(self.connections)

    def update_connection(self, conn_id, new_status):
        if conn_id in self.connections:
            self.connections[conn_id] = new_status

    def delete_connection(self, conn_id):
        if conn_id in self.connections:
            del self.connections[conn_id]


db = DatabaseHandler()
db.add_connection("XYZ", "Connected")
db.add_connection("ABC", "Disconnected")
db.display_connections()
db.update_connection("XYZ", "Disconnected")
db.delete_connection("ABC")
db.display_connections()