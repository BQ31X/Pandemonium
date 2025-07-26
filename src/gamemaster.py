from google.adk import Agent
from .spymaster import root_agent as spymaster_agent
from .operative import root_agent as operative_agent
from .operative import OperativeAgent
from .spymaster import SpymasterAgent
import os
class GameMasterAgent(Agent):
    def __init__(self):
        """Initialize the GameMasterAgent with a specific model and description."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(base_dir, "..", "instructions", "gamemasterprompt.txt")
        with open(prompt_path, "r") as f:
            instructions = f.read()
        # Initialize the base Agent class with specific parameters
        super().__init__(
            name="GameMasterAgent",
            model="gemini-2.0-flash",
            description="Game master that orchestrates the Codenames game",
            instruction=instructions

        )

root_agent = GameMasterAgent()


