import asyncio
from agents import Runner, RunConfig, TResponseInputItem, RunResult, OpenAIProvider
from typing import List, Dict, Any
from openai import AsyncOpenAI
from evaluator import evaluator, EvaluationFeedback
from requirement_generator import requirement_generator
from tool import RequirementModel

provider = OpenAIProvider(
    openai_client=AsyncOpenAI(base_url="base_url", api_key='api_key'),
    use_responses=False,
)

async def main() -> None:
    msg: str = input("What kind of ATM system would you like to design? ")
    input_items: List[TResponseInputItem] = [{"content": msg, "role": "user"}]
    latest_model: RequirementModel | None = None

    while True:
        requirement_result: RunResult = await Runner.run(
            requirement_generator,
            input_items,
            run_config=RunConfig(model_provider=provider)
        )
        input_items: List[TResponseInputItem] = requirement_result.to_input_list()
        latest_model = requirement_result.final_output_as(RequirementModel)
        print("Requirement model generated")
        print(latest_model)

        evaluator_result: RunResult = await Runner.run(
            evaluator,
            input_items,
            run_config=RunConfig(model_provider=provider)
        )
        result: EvaluationFeedback = evaluator_result.final_output
        print(f"Evaluator score: {result.score}")

        if result.score == "pass":
            print("Requirement model is good enough, exiting.")
            break

        print(result.feedback)
        print("Re-running with feedback")
        input_items.append({"content": f"Feedback: {result.feedback}", "role": "user"})

    print(f"Final requirement model: {latest_model}")

if __name__ == "__main__":
    asyncio.run(main())