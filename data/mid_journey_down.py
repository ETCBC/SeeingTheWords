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

class Locate(Enum):
    prompt_0 = 0
    prompt_1 = 1
    prompt_2 = 2
    prompt_3 = 3
    prompt_4 = 4

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


if __name__ == "__main__":
    folder = "input/"
    sub_folder = ['raw_prompt_2', 'raw_prompt_3', 'raw_prompt_4']

    output = 'data_images/'
    folder_output = ['prompt_2', 'prompt_3', 'prompt_4']

    for x, location in enumerate(sub_folder):
        num = 0
        root = folder + location
        root_out = output+folder_output[x]
        image_num = len([images for images in os.listdir(root) if images.endswith(".png")])
        print(image_num)
        console = Console()
        tasks = [f"Images {n}" for n in range(1, image_num)]
        with console.status("[bold green]Downloading Image...") as status:
            for i in range(image_num):
                top_left, top_right, bottom_left, bottom_right = split_image(root + '/'+ str(i+1) + ".png")
                # Save the output images with dynamic names in the output folder
                top_left.save(os.path.join(root_out + "/" + "mid_journey_" + str(num) + ".png"))
                top_right.save(os.path.join(root_out + "/" + "mid_journey_" + str(num + 1) + ".png"))
                bottom_left.save(os.path.join(root_out + "/" + "mid_journey_" + str(num + 2) + ".png"))
                bottom_right.save(os.path.join(root_out + "/" + "mid_journey_" + str(num + 3) + ".png"))
                num += 4

        task = tasks.pop(0)
        console.log(f"{task} downloaded to {root}")
