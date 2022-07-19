#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""

import redis
import requests
from typing import Callable
from functools import wraps


_redis = redis


def request_counter(method: Callable) -> Callable:
    """
    Counts how many times a request was made.
    """

    @wraps(method)
    def wrapper(url):
        """
        Decorator function
        """
        _redis.incr(f"count:{url}")
        html = _redis.get(f"cached:{url}")
        if html:
            decoded_html = html.decode('utf-8')
            return html

        html = method(url)
        _redis.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@request_counter
def get_page(url: str) -> str:
    """
    Uses the requests module to obtain the HTML
    content of a particular URL and returns it.
    """

    return requests.get(url).text
