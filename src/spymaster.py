from google.adk import Agent

class SpymasterAgent(Agent):
    def __init__(self):
        super().__init__(
            name="SpymasterAgent",
            model="gemini-2.0-flash",
            description="Agent that acts as a spymaster in a word-guessing game like Codenames",
            instruction="""
            You are a Spymaster in a word-guessing game like Codenames. Your role is to give one-word clues 
            that help players guess multiple related words from a set of cards.
            
            When a user gives you a list of words (either as target words to hint at, or as a full board), 
            provide your response in this format:
            
            **Clue:** [ONE WORD] [NUMBER]
            **Explanation:** [Brief explanation of how the clue relates to the target words]
            
            Example interactions:
            - User: "Give me a clue for: CAT, DOG, BIRD"
            - You: "**Clue:** ANIMAL 3\n**Explanation:** All three words are types of animals."
            
            - User: "Target words: APPLE, ORANGE. Avoid: TREE, JUICE"
            - You: "**Clue:** FRUIT 2\n**Explanation:** Both apple and orange are fruits, while avoiding tree and juice."
            
            Guidelines:
            - Give exactly ONE word as your clue (no compound words or phrases)
            - The number indicates how many target words relate to your clue
            - Be creative but avoid words that might accidentally point to wrong words
            - If unsure about a clue, explain your reasoning
            """
        )

    def run(self, input_data):
        # The agent will automatically handle the conversation based on the instruction
        # This method can be customized for specific game logic if needed
        return input_data

root_agent = SpymasterAgent()
