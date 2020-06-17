
class Content:
    def __init__(self):
        self.store = {}        # cache_id : content_id
        self.reverse_store = {}     # content_id: url

    def add_node(self, s_data, r_data):
        self.store.update(s_data)
        self.reverse_store.update(r_data)

    def read_reserve(self, key):
        if key in self.reverse_store:
            return {'url': self.reverse_store[key]}
        else:
            return {'url': None}

    def read_node(self, key):
        if key in self.store:
            return {'hash': self.store[key]}
        else:
            return {'hash': None}
