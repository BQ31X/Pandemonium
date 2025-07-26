from google.adk import Agent
import os
class OperativeAgent(Agent):
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(base_dir, "..", "instructions", "gamemasterprompt.txt")
        with open(prompt_path, "r") as f:
            instructions = f.read()
        super().__init__(
            name="OperativeAgent",
            model="gemini-2.0-flash",
            description="Operative agent that guesses words based on spymaster clues",
            instruction="You are an operative. When given a clue and number, guess words that relate to that clue."
        )

root_agent = OperativeAgent()
