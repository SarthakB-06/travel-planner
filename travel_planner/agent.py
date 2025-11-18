from google.adk.agents import Agent

from travel_planner.supporting_agents import inspiration_agent


root_agent = Agent(
    model="gemini-2.5-flash-lite",
    name="travel_planner_root_agent",
    description=" A helpful travel planning assistant that helps users plan their trips effectively and efficiently",
    instruction="""
    - You are an exclusive travel concierge agent.
    - You help users discover their dream holiday destination and plan their vacation.
    - Use the inspiration_agent to get the best destination, news, places nearby eg Hotels, cafes, attractions etc.
    - You cannot use any tool directly 
""",
    sub_agents=[inspiration_agent]
)