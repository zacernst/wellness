#! python

from openai import OpenAI
from typing import Optional

import click


client = OpenAI()

PROMPT = """Write a one-sentence, banal compliment about a person's specific abilities or small, trivial past accomplishments that have vague, but positive emotional connotations. For example, "You can set up a tent in under two minutes" or "You are an expert stargazer." The compliment should be very specific, so that they would not apply to most people. For example, "You have a good sense of humor" would be too general, and would apply to too many people. These compliment should be likely to cause a person hearing them to smile just a little bit. Avoid using superlatives that are too general, such as "perfect", "amazing", "great", or "best". The ideal compliment would indicate a small personality quirk or some trait that is somewhat unique to that person. Upon hearing each compliment, a person should feel that the speaker somehow knows them a bit better than expected. It is better if it is truly novel; it should be tasteful and appropriate, but it should be unlikely that anyone has heard such a compliment before. The compliment should not explicitly attribute abilities to the person; avoid phrases such as "knows how to", "has the ability to", "seems to", or "has a talent for". It should be stated in an active manner, suggesting agency on the part of the person. For example, do not say that the person "ends up with the right amount of ice". Instead say that the person "adds the right amount of ice to their drink." Express the compliment by referring to the person as "Your outtie", as in, 'Your outtie always knows when someone will enjoy a movie.'  """


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
