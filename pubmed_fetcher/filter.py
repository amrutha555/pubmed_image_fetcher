import re
from typing import List, Dict, Tuple

NON_ACADEMIC_KEYWORDS = ["pharma", "biotech", "inc.", "ltd.", "gmbh", "corporation", "therapeutics"]

def filter_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    """Filters papers to include only those with at least one non-academic author."""
    filtered_papers = []
    
    for paper in papers:
        authors = paper.get("authors", [])
        non_academic_authors, company_names = [], []
        
        for author in authors:
            if any(word in author.get("affiliation", "").lower() for word in NON_ACADEMIC_KEYWORDS):
                non_academic_authors.append(author["name"])
                company_names.append(author["affiliation"])
        
        if non_academic_authors:
            paper["non_academic_authors"] = ", ".join(non_academic_authors)
            paper["company_affiliations"] = ", ".join(set(company_names))
            filtered_papers.append(paper)
    
    return filtered_papers
