import json
from typing import List, Annotated, Any
from crewai.tools import BaseTool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from pydantic import model_validator, field_validator, Field

class WebSearchTool(BaseTool):
    """Tool that searches the web for information about Osvaldo Romberg."""
    
    name: str = "Web Search"
    description: str = "Search the web for information about Osvaldo Romberg"
    search_wrapper: Any = Field(default_factory=DuckDuckGoSearchAPIWrapper)
    
    def _run(self, query: Annotated[str, "The search query to look up"]) -> str:
        """Use the tool."""
        return self.search_wrapper.run(query)

class JSONDataSearchTool(BaseTool):
    """Tool that searches through local JSON data about Osvaldo Romberg."""
    
    name: str = "JSON Data Search"
    description: str = "Search through local JSON data about Osvaldo Romberg"
    
    def _run(self, query: Annotated[str, "The search query to look up in the JSON data"]) -> str:
        """Use the tool."""
        # Implement JSON search logic here
        results = []
        # Add your JSON search implementation
        return str(results)

class SearchTools:
    def __init__(self):
        self.search = DuckDuckGoSearchAPIWrapper()
        
    def load_json_data(self, file_path: str) -> dict:
        with open(file_path, 'r') as file:
            return json.load(file)
        
    def get_tools(self) -> List[BaseTool]:
        return [
            WebSearchTool(search_wrapper=self.search),
            JSONDataSearchTool()
        ] 