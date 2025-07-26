from google.adk import Agent
import os

class SpymasterAgent(Agent):
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Check for debug mode
        debug_mode = os.getenv('SPYMASTER_DEBUG_MODE', 'false').lower() == 'true'
        
        if debug_mode:
            # Load debug version with reasoning shown
            prompt_path = os.path.join(base_dir, "..", "instructions", "spymasterprompt_debug.txt")
        else:
            # Load production version with clean output only
            prompt_path = os.path.join(base_dir, "..", "instructions", "spymasterprompt_production.txt")
        
        # Fallback to original if specific files don't exist
        if not os.path.exists(prompt_path):
            prompt_path = os.path.join(base_dir, "..", "instructions", "spymasterprompt.txt")
            
        with open(prompt_path, "r") as f:
            instructions = f.read()
            
        super().__init__(
            name="SpymasterAgent",
            model="gemini-2.0-flash",
            description="Agent that acts as a spymaster in a word-guessing game like Codenames",
            instruction=instructions
        )

    def run(self, input_data):
        # The agent will automatically handle the conversation based on the instruction
        # This method can be customized for specific game logic if needed
        return input_data

root_agent = SpymasterAgent()
