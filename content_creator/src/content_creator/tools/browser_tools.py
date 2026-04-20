from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from bs4 import BeautifulSoup
import requests


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


class BrowserToolInput(BaseModel):
    url: str = Field(..., description="The URL to scrape.")


class BrowserTools(BaseTool):
    name: str = "Browser Tool"
    description: str = (
        "Scrapes a website URL and returns its content and links. "
        "Use this to read product pages, competitor sites, or any web content."
    )
    args_schema: Type[BaseModel] = BrowserToolInput

    def _run(self, url: str) -> str:
        return self.scrape_and_summarize_website(url)

    def scrape_and_summarize_website(self, url: str) -> str:
        content = self._fetch_contents(url)
        links = self._fetch_links(url)
        links_text = "\n".join(links[:10])  # top 10 links
        return f"{content}\n\nLinks found:\n{links_text}"

    def _fetch_contents(self, url: str) -> str:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string if soup.title else "No title found"
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            text = soup.body.get_text(separator="\n", strip=True)
        else:
            text = ""
        return (title + "\n\n" + text)[:2_000]

    def _fetch_links(self, url: str) -> list[str]:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        links = [link.get("href") for link in soup.find_all("a")]
        return [link for link in links if link]