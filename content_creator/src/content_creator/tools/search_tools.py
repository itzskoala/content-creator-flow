from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
import os


class SearchToolInput(BaseModel):
    query: str = Field(..., description="The search query to run.")
    search_type: str = Field(
        default="internet",
        description="'internet' for web search, 'social' for social media content."
    )


class SearchTools(BaseTool):
    name: str = "Search Tool"
    description: str = (
        "Searches the web or social media. "
        "Use search_type='internet' for market/competitor research. "
        "Use search_type='social' for trending posts and viral content."
    )
    args_schema: Type[BaseModel] = SearchToolInput

    def _run(self, query: str, search_type: str = "internet") -> str:
        if search_type == "social":
            return self.search_social_media(query)
        return self.search_internet(query)

    def search_internet(self, query: str) -> str:
        response = requests.post(
            "https://google.serper.dev/search",
            headers={"X-API-KEY": os.getenv("SERPER_API_KEY"), "Content-Type": "application/json"},
            json={"q": query, "num": 5},
            timeout=10
        )
        results = response.json().get("organic", [])
        return "\n\n".join(
            f"{i}. {r.get('title')}\n   {r.get('link')}\n   {r.get('snippet')}"
            for i, r in enumerate(results, 1)
        ) or "No results found."

    def search_social_media(self, query: str) -> str:
        social_query = query + " site:tiktok.com OR site:instagram.com OR site:linkedin.com OR site:twitter.com"
        response = requests.post(
            "https://google.serper.dev/search",
            headers={"X-API-KEY": os.getenv("SERPER_API_KEY"), "Content-Type": "application/json"},
            json={"q": social_query, "num": 5},
            timeout=10
        )
        results = response.json().get("organic", [])
        return "\n\n".join(
            f"{i}. {r.get('title')}\n   {r.get('link')}\n   {r.get('snippet')}"
            for i, r in enumerate(results, 1)
        ) or "No results found."