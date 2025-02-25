# Wellness

This trivial CLI tool takes an optional topic and generates a fact about your outtie. Because your outtie is an exemplary person, these facts should be pleasing to you.

## Usage

After installing, just type `wellness [topic]`. The topic is optional, but if you do provide a topic, put it in quotes if it's more than one word.

Here are some samples:

```
% wellness "room ventilation"
Your outtie excels at finding the perfect balance between opening and closing windows to create just the right airflow in any room.
% wellness "dogs"
Your outtie can always predict a dog's next move during playtime.
% wellness "Python programming"
Your outtie has a knack for using list comprehensions in Python that always impresses those around them.
% wellness "long train rides"  
Your outtie always finds the coziest spot by the window on long train rides.
% wellness "vegetables"      
Your outtie effortlessly selects the ripest tomatoes every time they go grocery shopping.
% wellness "swimming"
Your outtie effortlessly executes a flawless cannonball dive each time they hit the pool.
```

## Requirements

You'll need (for now) an API key from OpenAI. Set the environment variable `OPENAI_API_KEY` to your key. Then download this repository and do:

```
pip install .
```

Then you should have the `wellness` command available.

Try to enjoy each fact equally.


<img src="chair.jpg" alt="wellness" style="height: 100px;"/>