import urllib
import urllib.request
from urllib.error import HTTPError, URLError
from angaa.resources import chat


class Angaa:

    TIMEOUT_IN_SECS = 300

    def __init__(self, base_url: str, api_key: str = None, **kwargs):
        self.base_url = base_url
        self.api_key = api_key
        self.chat = chat.Chat(self)

    def _composeHeaders(self):
        headers = {}
        headers["Content-Type"] = "application/json"
        headers["Authorization"] = self.api_key
        return headers

    def _composeRequest(self, body: str | None, suffix: str | None):
        url = f"{self.base_url}/{suffix}"

        encoded_data = None
        if body:
            encoded_data = body.encode("utf-8")  # data should be bytes

        req = urllib.request.Request(url, data=encoded_data)
        for header, value in self._composeHeaders().items():
            req.add_header(header, value)
        return req

    def performRequest(self, body, suffix):
        request = self._composeRequest(body, suffix)

        try:
            response = (
                urllib.request.urlopen(request, timeout=Angaa.TIMEOUT_IN_SECS)
                .read()
                .decode("utf-8")
            )
            return response
        except HTTPError as error:
            print(error.status, error.reason)
        except URLError as error:
            print(error.reason)
        except TimeoutError:
            print("Request timed out")
