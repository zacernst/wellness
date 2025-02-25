"""
Praise Kier
"""

import os
import pathlib
import random
from typing import List, Optional

import click
from openai import OpenAI

client = OpenAI()

PROMPT_PATH = pathlib.Path(__file__).parent / "PROMPT.txt"
with open(PROMPT_PATH, "r") as f:
    PROMPTS = f.read().split("\n")


@click.group()
def main():
    pass


@main.command()
@click.argument("topic", default="")
def wellness(topic: Optional[str]):
    """Generate a pleasing fact about your outtie."""
    prompt = random.choice(PROMPTS)
    if topic:
        prompt += f" The topic of the statement should be '{topic}'."

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a gifted writer who is good friends with the user.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    response = completion.choices[0].message.content
    click.echo(response)


if __name__ == "__main__":
    wellness()
