from openai import AsyncOpenAI
import asyncio
import json5
import os
from dotenv import load_dotenv
from hitesh_chaudhary_system_prompt import system_prompt as hitesh_prompt
from piyush_garg_system_prompt import system_prompt as piyush_prompt

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL")


async def start_new_chat():
    persona = str(input("Who you wanna talk with Hitesh sir or Piyush sir?"))
    personality = ""
    
    system_prompt = ""
    if(persona[0].lower() == 'h'):
        system_prompt = hitesh_prompt
        personality = "Hitesh Sir"
    elif(persona[0].lower() == 'p'):
        system_prompt = piyush_prompt
        personality = "Piyush Sir"
    else:
        raise ValueError("persona didnt' exist!!!")
    
    client = AsyncOpenAI(
        api_key=api_key,
        base_url=base_url
    )
    messages: list[dict] = [
        {"role": "system", "content": system_prompt}
    ]
    while(True):
        query: str = str(input("~ "))
        messages.append({"role": "user", "content": query})
        response = await client.chat.completions.create(
            model=model,
            messages=messages,
            max_completion_tokens=500,
            temperature=0.7
        )
        content = response.choices[0].message.content
        result = {}
        try:
            result = json5.loads(str(content))
        except Exception as e:
            messages.append({"role": "assistant", "Content": "Response is not in json format pls revaluate and send correct output"})
            continue

        print(f'🤖{personality}: {result["content"]}')
        if(result["Step"] == "OUTPUT"):
            break
        messages.append({"role": "assistant", "content": content})


if __name__ == "__main__":
    asyncio.run(start_new_chat())