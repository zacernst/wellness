#! env python

import os

from openai import OpenAI
from typing import Optional

import click


client = OpenAI()

with open('PROMPT.txt', 'r', 'utf8') as f:
    PROMPT = f.read()


@click.group()
def main():
    pass


@main.command()
@click.argument("topic", default="")
def wellness(topic: Optional[str] = ""):
    if topic:
        prompt = PROMPT + f"The topic of the compliment should be '{topic}'."
    else:
        prompt = PROMPT

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    response = completion.choices[0].message.content
    print(response)
    return response


if __name__ == "__main__":
    click.echo(wellness())
