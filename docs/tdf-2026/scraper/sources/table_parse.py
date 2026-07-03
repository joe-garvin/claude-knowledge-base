"""Generic header-driven HTML table parsing, shared by the PCS and
Wikipedia scrapers. Locating columns by header text (rather than fixed
positions) survives minor markup reshuffles better than hard-coded
indices — at the cost of being fooled by an unexpected header wording
change, which is exactly the kind of failure the contract validation in
scrape.py is meant to catch and fall back from, not crash on.
"""

import re


def find_table_by_header(soup, required_header_substring):
    for table in soup.find_all("table"):
        header_cells = [th.get_text(strip=True).lower() for th in table.find_all("th")]
        if any(required_header_substring in h for h in header_cells):
            return table, header_cells
    return None, None


def column_index(headers, *names):
    for name in names:
        for i, h in enumerate(headers):
            if name in h:
                return i
    return None


def cell_text(cells, index):
    if index is None or index >= len(cells):
        return None
    link = cells[index].find("a")
    text = (link or cells[index]).get_text(strip=True)
    return text or None


def parse_rank(text, fallback):
    if not text:
        return fallback
    digits = re.sub(r"[^0-9]", "", text)
    return int(digits) if digits else fallback
