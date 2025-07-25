from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

# --- Define AgentC: The final recipient / reporter ---
class AgentC(Agent):
    def __init__(self):
        super().__init__(
            name="AgentC",
            model="gemini-2.0-flash",
            description="Agent C receives a message and prepares it for the user.",
            instruction="""
            You are Agent C in the Telephone Game. You have received a message that has been passed through Agent A and Agent B.
            Your task is to simply present the final message clearly to the user, wrapped in <FINAL_MESSAGE> tags.
            Do not add any new details or modify the message further. Just output the message exactly as you received it.
            """
        )

# --- Define AgentB: Modifies and returns ---
class AgentB(Agent):
    def __init__(self):
        super().__init__(
            name="AgentB",
            model="gemini-2.0-flash",
            description="Agent B receives a message, adds a subtle detail, and returns the modified message.",
            instruction="""
            You are Agent B in the Telephone Game. You have received a message from Agent A.
            Your task is to add *one single, very subtle, and creative detail* to the message, and then return this modified message.
            
            Important guidelines:
            - Do NOT change the core meaning of the message
            - The detail should be small and almost unnoticeable
            - Simply return the modified message without any additional commentary
            - Do not say "Here's the modified message" or similar - just return the message itself
            """
        )

# --- Define AgentA: Modifies and returns ---
class AgentA(Agent):
    def __init__(self):
        super().__init__(
            name="AgentA",
            model="gemini-2.0-flash",
            description="Agent A receives a message, adds a subtle detail, and returns the modified message.",
            instruction="""
            You are Agent A in the Telephone Game. You have received an initial message from the user.
            Your task is to add *one single, very subtle, and creative detail* to the message, and then return this modified message.
            
            Important guidelines:
            - Do NOT change the core meaning of the message
            - The detail should be small and almost unnoticeable
            - Simply return the modified message without any additional commentary
            - Do not say "Here's the modified message" or similar - just return the message itself
            """
        )

# --- Main Orchestration Agent ---
class TelephoneOrchestrator(Agent):
    def __init__(self):
        # Create instances of the specialized agents
        agent_a_instance = AgentA()
        agent_b_instance = AgentB()
        agent_c_instance = AgentC()

        # Wrap agents as tools using AgentTool
        agent_a_tool = AgentTool(agent=agent_a_instance)
        agent_b_tool = AgentTool(agent=agent_b_instance)
        agent_c_tool = AgentTool(agent=agent_c_instance)

        super().__init__(
            name="TelephoneGameMaster",
            model="gemini-2.0-flash",
            description="Orchestrates the Telephone game by passing a message sequentially through Agent A, then Agent B, then Agent C.",
            instruction="""
            You are the Telephone Game Master. When you receive an initial message from the user, you must orchestrate the telephone game by calling the agents in sequence:

            1. First, call AgentA with the user's original message
            2. Then, call AgentB with the response from AgentA  
            3. Finally, call AgentC with the response from AgentB
            4. Present the final result to the user

            Always explain what's happening at each step so the user can see how the message evolves through the telephone game.

            Example flow:
            "Starting the telephone game with your message: '[original message]'
            
            Step 1: Passing to Agent A...
            Agent A says: '[Agent A response]'
            
            Step 2: Passing Agent A's message to Agent B...
            Agent B says: '[Agent B response]'
            
            Step 3: Passing Agent B's message to Agent C...
            Agent C says: '[Agent C response]'
            
            The telephone game is complete! Here's how your message evolved through the chain."
            """,
            tools=[agent_a_tool, agent_b_tool, agent_c_tool]
        )

# Make this the root agent for ADK to discover when running `adk web`
root_agent = TelephoneOrchestrator()