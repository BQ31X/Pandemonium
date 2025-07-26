from google.adk import Agent
import os
class OperativeAgent(Agent):
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(base_dir, "..", "instructions", "operativeprompt.txt")
        with open(prompt_path, "r") as f:
            instructions = f.read()
        super().__init__(
            name="OperativeAgent",
            model="gemini-2.0-flash",
            description="Operative agent that guesses words based on spymaster clues",
            instruction=instructions
        )

root_agent = OperativeAgent()
