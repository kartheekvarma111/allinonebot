import logging
import time
from typing import Optional
import requests
from requests.exceptions import RequestException

# Logging
logger = logging.getLogger(__name__)

def make_request(url: str, retries: int = 6, timeout: int = 12) -> Optional[requests.Response]:
    # Proxy (uncomment and set if needed)
    # proxies = {'http': 'http://your_proxy_ip:port', 'https': 'http://your_proxy_ip:port'}  # Ex: 'http://123.45.67.89:8080'
    proxies = None
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=timeout, proxies=proxies)
            response.raise_for_status()
            logger.debug(f"Successful request to {url}")
            return response
        except RequestException as e:
            logger.warning(f"Request failed for {url}, attempt {attempt + 1}/{retries}: {str(e)}")
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                logger.error(f"All {retries} attempts failed for {url}")
                return None
    return None