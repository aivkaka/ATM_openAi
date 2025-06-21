from imaplib import Literal
from agents import Agent


class EvaluationFeedback:
    score: Literal["pass", "needs_improvement", "fail"]
    feedback: str

evaluator = Agent(
    name="evaluator",
    model="gpt-4o",
    instructions=(
        "You are an evaluator. Evaluate the generated requirement model for an ATM system."
        "Provide feedback on what needs to be improved if it's not good enough."
        "Never give it a pass on the first try."
    ),
    output_type=EvaluationFeedback,
)