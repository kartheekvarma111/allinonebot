import logging
from typing import List, Dict
from bs4 import BeautifulSoup
from .utils import make_request

logger = logging.getLogger(__name__)

async def netnaija_web_scrapper(search_term: str) -> List[Dict[str, str]]:
    search_term = search_term.replace(' ', '+')
    base_url = f"https://www.thenetnaija.co/search?t={search_term}"
    
    try:
        response = make_request(base_url)
        if not response:
            logger.error(f"No response from Netnaija for {search_term}")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        for article in soup.select('article.post'):
            title_elem = article.select_one('h2.post-title a')
            link_elem = article.select_one('h2.post-title a')
            if title_elem and link_elem:
                title = title_elem.text.strip()
                link = link_elem['href']
                results.append({
                    'text': title,
                    'url': link
                })
        
        logger.info(f"Found {len(results)} Netnaija links for {search_term}")
        return results
    except Exception as e:
        logger.error(f"Netnaija scraper error for {search_term}: {str(e)}")
        return []