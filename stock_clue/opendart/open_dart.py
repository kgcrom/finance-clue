import requests
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from stock_clue.opendart.disclosure import Disclosure


class OpenDart(object):

    def __init__(self, api_key: str):
        super().__init__()
        self.api_key = api_key
        self.base_url = 'https://opendart.fss.or.kr'

    @property
    def disclosure(self) -> "Disclosure":
        from stock_clue.opendart import disclosure
        return disclosure.Disclosure(self)

    def get(self, path: str, params: Dict) -> requests.Response:
        params['crtfc_key'] = self.api_key
        return requests.get(f'{self.base_url}{path}', params)
