from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class SearchToolInput(BaseModel):
    """Input schema for SearchTool."""
    query: str = Field(..., description="The search query.")

class SearchTools(BaseTool):
    name: str = "Search Tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = SearchToolInput

    # def _run(self, query: str) -> str:
    #     # Implementation goes here
    #     return "this is an example of a tool output, ignore it and move along."
    
    def search_internet(self, query: str) -> str:
        # Implementation to search the internet goes here
        return f"Searching the internet for: {query}"
    
    def search_social_media(self, query: str) -> str:
        # Implementation to search social media platforms goes here
        return f"Searching social media for: {query}"
    
    

