import json
from typing import List
from langchain.tools import Tool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

class SearchTools:
    def __init__(self):
        self.search = DuckDuckGoSearchAPIWrapper()
        
    def load_json_data(self, file_path: str) -> dict:
        with open(file_path, 'r') as file:
            return json.load(file)
            
    def search_json_data(self, tool_input: str, data: dict = None) -> List[str]:
        # Implement JSON search logic here
        results = []
        # Add your JSON search implementation
        return results
        
    def web_search(self, tool_input: str) -> str:
        return self.search.run(tool_input)
        
    def get_tools(self) -> List[Tool]:
        return [
            Tool(
                name="Web Search",
                func=self.web_search,
                description="Search the web for information about Osvaldo Romberg"
            ),
            Tool(
                name="JSON Data Search",
                func=self.search_json_data,
                description="Search through local JSON data about Osvaldo Romberg"
            )
        ] 