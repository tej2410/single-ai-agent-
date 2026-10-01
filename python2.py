

# import asyncio
# import os
#
# from autogen_agentchat.agents import AssistantAgent
# from autogen_agentchat.ui import Console
# from autogen_ext.models.openai import OpenAIChatCompletionClient
#
#
# os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE"
#
#
# async def main2():
#     print("I am creating an Agentic AI project")
#
#     model_client = OpenAIChatCompletionClient(
#         model="gpt-4o"
#     )
#
#     assistant = AssistantAgent(
#         name="assistant",
#         model_client=model_client
#     )
#
#     await Console(
#         assistant.run_stream(
#             task="What is 17 * 7?"
#         )
#     )
#
#     await model_client.close()
#
#
# if __name__ == "__main__":
#     asyncio.run(main2())
#
#


import asyncio


async def main2():
    print("I am creating an Agentic AI project")

    question = "What is 17 * 7?"
    answer = 17 * 7

    print("\nAssistant:")
    print(f"The answer is {answer}.")


if __name__ == "__main__":
    asyncio.run(main2())
