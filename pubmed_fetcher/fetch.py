import requests
from typing import List, Dict

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_pubmed_papers(query: str, max_results: int = 10) -> List[Dict]:
    """Fetches research papers from PubMed based on a query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    
    paper_ids = response.json().get("esearchresult", {}).get("idlist", [])
    return get_paper_details(paper_ids)

def get_paper_details(paper_ids: List[str]) -> List[Dict]:
    """Fetches details of papers using their PubMed IDs."""
    if not paper_ids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    response = requests.get(DETAILS_URL, params=params)
    response.raise_for_status()
    
    summaries = response.json().get("result", {})
    return [summaries[pid] for pid in paper_ids if pid in summaries]
