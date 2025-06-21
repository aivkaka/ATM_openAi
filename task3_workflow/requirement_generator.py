from agents import Agent
from tool import generate_use_case, generate_requirement_model

requirement_generator = Agent(
    name="requirement_generator",
    model="gpt-4o",
    instructions=(
        "You are a requirements analyst. Generate a detailed requirement model for an ATM system based on the user's input."
        "The model should include system name, roles, modules with descriptions and flows, and use cases."
        "Use the provided tools to create structured output in JSON format."
    ),
    tools=[generate_use_case, generate_requirement_model],
)
