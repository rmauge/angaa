from angaa.resources.completions import Completions


class Chat:
    def __init__(self, client):
        self.client = client
        self.completions = Completions(self.client)
