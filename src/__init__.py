# You could change this line to import from any filename:
# from .day_trip import root_agent        # ← Current
# from .telephone_game import root_agent  # ← If you rename the file
# from .my_agent import root_agent        # ← Or any name you want

from .telephone_game import root_agent

# Export the agent so it can be discovered by ADK
__all__ = ['root_agent']
