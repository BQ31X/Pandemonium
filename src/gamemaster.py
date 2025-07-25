from google.adk import Agent

class GameMasterAgent(Agent):
    def __init__(self):
        super().__init__(
            name="GameMasterAgent",
            model="gemini-2.0-flash",
            description="Game master that orchestrates the Codenames game",
            instruction="You are a game master. You coordinate between the spymaster and operatives in a word game."
        )

root_agent = GameMasterAgent()
