from dataclasses import dataclass

@dataclass
class Analysis:
    """ Holds an analyzed post-mortem or plan """
    title: str
    url: str
    source_agency: str
    summary: str
    full_text: str
    paragraphs: list[str]
    keywords: list[str]
    key_ideas: list[str]