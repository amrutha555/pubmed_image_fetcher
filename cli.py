import click
import logging
from pubmed_fetcher.fetch import fetch_pubmed_papers
from pubmed_fetcher.filter import filter_non_academic_authors
from pubmed_fetcher.export import export_to_csv

@click.command()
@click.argument("query")
@click.option("-f", "--file", type=str, default=None, help="Output CSV filename.")
@click.option("-d", "--debug", is_flag=True, help="Enable debug mode.")
def main(query: str, file: str, debug: bool):
    """Fetches and filters PubMed research papers."""
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    
    logging.info("Fetching papers from PubMed...")
    papers = fetch_pubmed_papers(query)
    
    logging.info("Filtering for non-academic authors...")
    filtered_papers = filter_non_academic_authors(papers)
    
    if file:
        export_to_csv(filtered_papers, file)
        click.echo(f"Results saved to {file}")
    else:
        for paper in filtered_papers:
            click.echo(f"{paper['uid']}: {paper['title']}")

if __name__ == "__main__":
    main()
