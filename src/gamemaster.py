from random import random

from .operative import OperativeAgent
from .spymaster import SpymasterAgent
import os
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.agents.invocation_context import InvocationContext
#from shared_word_pool import get_words_by_category, ALL_WORDS
from .spymaster_tester import main
class GameMasterAgent(Agent):

    def build_initial_wordlist(red_count=3, blue_count=2, neutral_count=2, assassin_count=1, category=None):
        """Generate a test prompt with target words and different types of avoid words."""
        # Use shared word pool for consistent generation
        return "Target words (red): FORTNITE, BATTERY, SPIDERMAN. Opponent words (blue): DOG. Civilian words (neutral): FLEX. ASSASSIN: VIRAL"

    def __init__(self):
        """Initialize the GameMasterAgent with a specific model and description."""
        operative_agent_instance = OperativeAgent()
        spymaster_agent_instance = SpymasterAgent()
        initial_list_words = main()
        print(f"Initial word list generated: {initial_list_words}")
        #ctx = InvocationContext()
        #ctx.session.state['board_words'] = ["FORTNITE", "BATTERY", "SPIDERMAN","DOG","FLEX","viral"]  # Pass input via state
        #ctx.session.state['board_words_mapping'] = {"red": ["FORTNITE", "BATTERY", "SPIDERMAN"],
        #"blue":["DOG"],"civilian":["FLEX"],"assassin":"viral"}  # Pass input via state

        # Wrap agents as tools using AgentTool

        operative_agent = AgentTool(agent=operative_agent_instance)
        spymaster_agent = AgentTool(agent=spymaster_agent_instance)
        #boardwords_tool = Agent(tools=[self.build_initial_wordlist], name="BoardWordsTool", description="Generates the initial word list for the game")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(base_dir, "..", "instructions", "gamemasterprompt.txt")

        with open(prompt_path, "r") as f:
            instructions = f.read().replace("input_word_list_placeholder", str(initial_list_words))

        super().__init__(
            name="GameMasterAgent",
            model="gemini-2.0-flash",
            description="Game master that orchestrates the Codenames game",
            instruction=instructions,
            tools=[operative_agent, spymaster_agent]
        )

root_agent = GameMasterAgent()




