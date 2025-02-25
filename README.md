# Wellness

This trivial CLI tool takes an optional topic and generates a fact about your outtie. Because your outtie is an exemplary person, these facts should be pleasing to you.

## Usage

After installing, just type `wellness [topic]`. The topic is optional, but if you do provide a topic, put it in quotes if it's more than one word.

Here are some samples:

```
% wellness "long train rides"
Your outtie finds solace in listening to nostalgic songs during long train rides.
% wellness "dogs"
Your outtie always gets a little teary-eyed watching old dog movies.
% wellness
Your outtie can identify the perfect cookie-to-ice cream ratio for a delectable sandwich treat.
% wellness "declarative programming in Prolog"
Your outtie impressed everyone by successfully implementing a unique sorting algorithm in Prolog during a coding competition.
```

## Requirements

You'll need (for now) an API key from OpenAI. Set the environment variable `OPENAI_API_KEY` to your key. Then download this repository and do:

```
pip install .
```

Then you should have the `wellness` command available.

Try to enjoy each fact equally.


<img src="chair.jpg" alt="wellness" style="height: 100px;"/>