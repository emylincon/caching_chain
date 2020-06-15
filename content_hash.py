
class Content:
    def __init__(self):
        self.store = {}

    def add_node(self, data):
        self.store.update(data)

    def read_node(self, key):
        if key in self.store:
            return {'hash': self.store[key]}
        else:
            return {'hash': None}
