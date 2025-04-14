class MusicQueue:
    def __init__(self):
        self.queue = []

    def add(self, song):
        self.queue.append(song)

    def skip(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def get_all(self):
        return self.queue

queue = MusicQueue()