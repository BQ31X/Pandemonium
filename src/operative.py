from google.adk import Agent
from sentence_transformers import SentenceTransformer, util

class OperativeAgent(Agent):
    def __init__(self):
        super().__init__(
            name="OperativeAgent",
            model="gemini-2.0-flash",
            description="Operative agent that guesses words based on spymaster clues",
            instruction="""
You are an operative agent in the game Codenames.

Given:
- A clue (a word or phrase)
- A number (how many words relate to the clue)
- A list of board words

Your job:
1. Select the most semantically related words to the clue — up to the number given (and optionally +1 if guessing confidently).
2. Avoid selecting words that are likely to be the assassin, the opponent's, or civilians.
3. Prioritize words that share **meaning, category, association, or context** with the clue.
4. Avoid making guesses that feel unrelated to the clue even if similar in spelling or phonetics.
"""
        )

    def get_embedder(self):
        # Lazy load — ADK-safe
        if not hasattr(self, "_embedder"):
            self._embedder = SentenceTransformer('all-MiniLM-L6-v2')
        return self._embedder

    def act(self, clue: str, number: int, board_words: list, forbidden_words: list = []) -> list:
        """
        Given a clue, number of guesses, and board words, return best guesses based on embedding similarity.
        Avoids forbidden words (e.g., assassin, opponents).
        """
        embedder = self.get_embedder()

        clue_embedding = embedder.encode(clue, convert_to_tensor=True)
        board_embeddings = embedder.encode(board_words, convert_to_tensor=True)
        similarities = util.cos_sim(clue_embedding, board_embeddings)[0]

        # Rank by similarity
        scored_words = sorted(
            zip(board_words, similarities.tolist()),
            key=lambda x: -x[1]
        )

        # Filter forbidden and take top `number` guesses
        guesses = [word for word, _ in scored_words if word not in forbidden_words][:number]

        return guesses

root_agent = OperativeAgent()
