# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os
import re
import discord

from keep_up import keep_awake

from langchain import HuggingFaceHub
from langchain.agents import load_agent
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# langchain
repo_id = "baichuan-inc/Baichuan2-13B-Chat"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
llm = HuggingFaceHub(repo_id=repo_id,
                     model_kwargs={
                         "temperature": 0.1,
                         "max_new_tokens": 250
                     })

memory = ConversationBufferMemory()

conversation_chain = ConversationChain(llm=llm, verbose=True, memory=memory)


def generate_response(query):
  """Generates a chatbot response to the given query."""
  try:
    response = conversation_chain.predict(input=query)
  except Exception as e:
    response = f"I couldn't generate a response due to the following error: {str(e)}"
  # Strip the "Human:" string and the rest of the string after it
  response = re.sub(r'Human:.*', '', response, flags=re.DOTALL)

  return response


def conv_memory_dump():
  return "mem"


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$lang'):
    query = message.content[len('$lang '):]
    response = generate_response(query)
    await message.channel.send(response)

  if message.content.startswith('$mem'):
    response = conv_memory_dump()
    await message.channel.send(response)


try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
  if e.status == 429:
    print(
        "The Discord servers denied the connection for making too many requests"
    )
    print(
        "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
    )
  else:
    raise e

keep_awake()
