from google.adk import Agent

class OperativeAgent(Agent):
    def __init__(self):
        super().__init__(
            name="OperativeAgent",
            model="gemini-2.0-flash",
            description="Operative agent that guesses words based on spymaster clues",
            instruction="You are an operative. When given a clue and number, guess words that relate to that clue."
        )

root_agent = OperativeAgent()
