import json
from json import JSONDecodeError

import logging

import requests
from requests.models import Response

logger = logging.getLogger("test_rest_client")
BASE_URL = "https://poetrydb.org/"


def _init_request(uri: str, headers: dict):
    full_uri = f"{BASE_URL}/{uri}"
    return full_uri, headers


def get_request(uri: str, headers: dict = {}):
    full_uri, headers = _init_request(uri, headers)

    logger.info(f"Getting data to {full_uri} with headers {headers}")
    resp: Response = requests.get(full_uri, headers=headers)
    content = resp.text
    try:
        content = resp.json()
    except JSONDecodeError:
        logger.info("The response is not json")
    return resp.status_code, content
