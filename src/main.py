import os
from dotenv import load_dotenv
from crewai import Crew, Task
from agents.romberg_agent import RombergAgent
from tools.search_tools import SearchTools

# Load environment variables
load_dotenv()

def main():
    # Initialize tools
    search_tools = SearchTools()
    
    # Create Romberg agent
    romberg = RombergAgent.create()
    
    # Start chat loop
    print("Chat with Osvaldo Romberg (type 'exit' to quit)")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break
            
        # Create a task for each user input
        task = Task(
            description=user_input,
            agent=romberg,
            tools=search_tools.get_tools()
        )
        
        # Create crew with the current task
        crew = Crew(
            agents=[romberg],
            tasks=[task],
            verbose=True
        )
        
        # Execute the task
        response = crew.kickoff()
        print(f"\nOsvaldo: {response}")

if __name__ == "__main__":
    main() 