# import asyncio
# import os
#
# from autogen_agentchat.agents import AssistantAgent
# from autogen_agentchat.ui import Console
#
# from autogen_ext.models.openai import OpenAIChatCompletionClient
#
# import os
#
# # os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE"
#
#
#  os.environ["OPENAI_API_KEY"] = "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
#
#
# async def main():
#     model_client = OpenAIChatCompletionClient(
#         model="gpt-4o"
#     )
#
#     assistant = AssistantAgent(name="Assistant",model_client=model_client)
#     await Console(assistant.run_stream(task="what is 17* 7 ?"))
#     await model_client.close()
#
#     asyncio.run(main())

import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE"


async def main2():
    print("I am creating an Agentic AI project")

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o"
    )

    assistant = AssistantAgent(
        name="assistant",
        model_client=model_client
    )

    await Console(
        assistant.run_stream(
            task="What is 17 * 7?"
        )
    )

    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main2())


