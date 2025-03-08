import pandas as pd
from typing import List, Dict

def export_to_csv(papers: List[Dict], filename: str) -> None:
    """Exports filtered papers to a CSV file."""
    df = pd.DataFrame(papers, columns=[
        "uid", "title", "pubdate", "non_academic_authors", "company_affiliations"
    ])
    df.rename(columns={"uid": "PubmedID", "pubdate": "Publication Date"}, inplace=True)
    df.to_csv(filename, index=False)
