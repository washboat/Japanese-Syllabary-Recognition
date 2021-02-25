class DupeFilter(object):
    def __init__(self):
        self.messages = set()
        self.count = 0

    def filter_message(self, record):
        is_duplicate = record in self.messages
        self.messages.add(record)
        self.count += 1
        return is_duplicate, self.count

