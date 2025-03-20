import os
import textwrap
from dotenv import load_dotenv
from crewai import Crew, Task
from agents.romberg_agent import RombergAgent
from tools.search_tools import SearchTools
import elevenlabs
from elevenlabs import ElevenLabs
import tempfile
import subprocess
import platform

# Load environment variables
load_dotenv()

# Configure Eleven Labs
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "sk_3f46c0e7fd0df2e4a16a9577d1665d4bd99f645ee9cad0a9")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "din8A7JQYRv0G2HvK2w0")
eleven_labs = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def format_response(text):
    if hasattr(text, 'final_output'):
        text = text.final_output
    elif hasattr(text, 'raw_output'):
        text = text.raw_output
    # Convert to string if it's not already
    text = str(text)
    # Wrap text to 80 characters and remove extra whitespace
    wrapped_text = textwrap.fill(text.strip(), width=80, replace_whitespace=False)
    return wrapped_text

def speak_text(text):
    """Generate speech from text using Eleven Labs API and play it"""
    try:
        # Generate audio from text
        audio = eleven_labs.generate(
            text=text,
            voice=VOICE_ID,
            model="eleven_multilingual_v2",
            voice_settings={
                "stability": 0.26,
                "similarity_boost": 0.84,
                "style": 0.74,
                "use_speaker_boost": True,
                "speed": 1.0
            }
        )
        
        # Save to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        for chunk in audio:
            temp_file.write(chunk)
        temp_file.close()
        
        # Play the audio file based on the operating system
        system = platform.system()
        if system == "Darwin":  # macOS
            subprocess.call(["afplay", temp_file.name])
        elif system == "Windows":
            os.startfile(temp_file.name)
        else:  # Linux
            subprocess.call(["mpg123", temp_file.name])
            
        # Clean up
        os.unlink(temp_file.name)
    except Exception as e:
        print(f"Error generating or playing speech: {e}")

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
            tools=search_tools.get_tools(),
            expected_output="A conversational response from Osvaldo Romberg"
        )
        
        # Create crew with the current task
        crew = Crew(
            agents=[romberg],
            tasks=[task],
            verbose=True
        )
        
        # Execute the task and format the response
        response = crew.kickoff()
        formatted_response = format_response(response)
        print(f"\n{formatted_response}\n")
        
        # Speak the response
        speak_text(formatted_response)

if __name__ == "__main__":
    main() 