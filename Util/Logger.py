
class Logger:
    def __init__(self, filt):
        self.filter = filt
        self.count = 0

    def log_error(self, message):
        is_duplicate, self.count = self.filter.filter_message(message)
        if not is_duplicate:
            print(message)

    def add_filter(self, filter):
        self.filter = filter

    def remove_filter(self):
        del self.filter
