import json
import urllib
import urllib.request
from urllib.error import HTTPError, URLError

from angaa.entities.message import DeveloperMessage, SystemMessage, UserMessage


class Completions:
    URL_SUFFIX = "api/chat"

    def __init__(self, client):
        self.client = client

    def create(
        self,
        messages: list[UserMessage | DeveloperMessage | SystemMessage],
        model: str | None = "mistral:latest",
        stream: bool = False,
        response_format_type: str = None,
    ):
        data = {
            "model": model,
            "messages": [
                {"role": message.role.value, "content": message.content}
                for message in messages
            ],
            "stream": False,
        }

        if stream and "stream" in data:
            del data["stream"]

        if response_format_type:
            data["response_format"] = {"type": response_format_type}

        json_data = json.dumps(data)

        return self.client.performRequest(json_data, Completions.URL_SUFFIX)
