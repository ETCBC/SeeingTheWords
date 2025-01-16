import time
from enum import Enum
from rich.console import Console

import pyautogui as pg

from tqdm import tqdm
import asyncio
import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
from PIL import Image

import os

load_dotenv()
client = commands.Bot(command_prefix="*", intents=discord.Intents.all())
token = 'add-key'

class Locate(Enum):
    prompt_0 = 0
    prompt_1 = 1
    prompt_2 = 2
    prompt_3 = 3
    prompt_4 = 4
def prompt_download(prompts,location_prompt):
   try:
        prompt_list = []
        for prompt in prompts:
            print("reading prompts at " + str(location_prompt) + str(prompt))
            f = open(location_prompt + prompt, 'r')
            text = f.read().replace('\n', ' ').replace('\r', ' ')
            prompt_list.append(text)

        if  len(prompt_list) > 0:
            return prompt_list
   except:
       print("failed to read prompts")

def is_valid(m):
    return "(Waiting to start)" in m.content


async def keyboard_ctl(index):
    jobs = 0
    size = 5

    root_location = 'prompts/'
    prompt_text = ['prompt_0.txt', '    prompt_1.txt', 'prompt_2.txt', 'prompt_3.txt', 'prompt_4.txt']
    prompts = prompt_download(prompt_text, root_location)
    for i in tqdm(range(size), desc="bot creating images ...."):
        prompt = prompts[index]
        if jobs == 3:
            await asyncio.sleep(120)
            jobs = 0

        await asyncio.sleep(3)
        pg.press('tab')
        await asyncio.sleep(3)
        pg.write('/imagine')
        await asyncio.sleep(3)
        pg.press('tab')
        pg.write(prompt)
        await asyncio.sleep(5)
        pg.press('enter')

        jobs += 1

        try:
           await client.wait_for('message', check=is_valid, timeout=60)

        except asyncio.TimeoutError:
            print('time out error took to long to get verification for job')
            return
    return

def split_image(image_file):

        with Image.open(image_file) as im:
            # Get the width and height of the original image
            width, height = im.size
            # Calculate the middle points along the horizontal and vertical axes
            mid_x = width // 2
            mid_y = height // 2
            # Split the image into four equal parts
            top_left = im.crop((0, 0, mid_x, mid_y))
            top_right = im.crop((mid_x, 0, width, mid_y))
            bottom_left = im.crop((0, mid_y, mid_x, height))
            bottom_right = im.crop((mid_x, mid_y, width, height))
            return top_left, top_right, bottom_left, bottom_right


def download_image(images, filename, cat, num):
    folder = "data_images/" + Locate(cat).name
    response = requests.get(images)

    if response.status_code == 200:

        name = "input/" + filename
        with open(name, "wb") as f:
            f.write(response.content)
        # print(f"Image downloaded: {filename}")
        # input_file = os.path.join(input_folder, filename)

        if "UPSCALED_" not in filename:

            # Split the image
            top_left, top_right, bottom_left, bottom_right = split_image(name)
            # Save the output images with dynamic names in the output folder
            top_left.save(os.path.join(folder+"/" + "mid_journey_" + str(num) + ".jpg"))
            top_right.save(os.path.join(folder+"/" + "mid_journey_" + str(num + 1)  + ".jpg"))
            bottom_left.save(os.path.join(folder+"/" + "mid_journey_" + str(num + 2) + ".jpg"))
            bottom_right.save(os.path.join(folder+"/" + "mid_journey_" + str(num + 3)+ ".jpg"))
        # # else:
        #     os.rename(f"{directory}/{input_folder}/{filename}", f"{directory}/{output_folder}/{filename}")
        # # Delete the input file
        # os.remove(f"{directory}/{input_folder}/{filename}")


class MyBot(discord.Client):

    async def on_ready(self):
        print(f'logged in as {self.user} (ID: {self.user.id})')
        print('----')

    async def on_message(self, message):

        if message.author.id == self.user.id:
            return

        # use Discord message to download images from a channel history, example: "history:50"
        if message.content.startswith("history:"):

            download_qty = int(message.content.split(":")[1]) + 1
            cat = int(message.content.split(":")[2])
            channel = message.channel

            num = 1
            console = Console()
            tasks = [f"Images {n}" for n in range(1, download_qty + 1)]

            with console.status("[bold green]Downloading Image...") as status:
                async for msg in channel.history(limit=download_qty):

                    for attachment in msg.attachments:

                        if "Upscaled by" in message.content:
                            file_prefix = 'UPSCALED_'

                        else:
                            file_prefix = ''

                        if attachment.filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                            try:
                                download_image(attachment.url, f"{file_prefix}{attachment.filename}", cat, num)
                                num += 4

                            except:
                                time.sleep(10)
                                continue

                    task = tasks.pop(0)
                    console.log(f"{task} downloaded to {Locate(cat).name}")

        if message.content.startswith("make:"):
            prompt_index = int(message.content.split(":")[1])
            await keyboard_ctl(prompt_index)

@client.event
async def ready():
    print("Olli is up and running")

def test():
    @client.event
    async def on_message(message):
        msg = message.content
        print(message)
        print(msg)

    client.run('add key')

if __name__ == "__main__":

    intents = discord.Intents.default()
    intents.message_content = True
    client = MyBot(intents=intents)
    client.run(token)