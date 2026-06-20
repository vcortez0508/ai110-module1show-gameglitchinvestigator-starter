# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game was simple, yet it had multiple bugs theat were noticeable from the start.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. Difficulty leveles were inaccurate.
  2. "New Game" button does not start a new game. In fact, it did nothing.
  3. "Press Enter to guess" Did nothing. You are forced to press "Submit Guess". 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|   9   |    "Too low"      |    "Too High"   |       none visible     | 
|  none |ascending difficulty|Mixed difficulty|       none visible     |
| Enter | Submit the guess  |     Nothing     |       none visible     |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude for live-work/edits and ChatGpt for 
  more syntax/coding oriented questions such as git commands.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  One of the suggestions was just hard coding the difficulty levels by difficulty. It was a simple fix and when ran on a browser, the 
  fix worked seamlessly.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  the ai tried to create a test for one of the errors but, in the process would create a test for a different error as well (unprompted). 
  I verified by giving it a more specific task.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
  I mainly used claude to create tests through pytest. 
  The only manual way I verified my code was by running the game to verify the fixes were applied.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
A streamlit rerun is the just the entire script in your program being run from the top to the bottom any time you interact with the created app.

A session state is like a temporary memory that helps an app remember things about you while you're using it. Without it, the app would forget everything and start over every time you clicked a button or made a change.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.
  Definitely the idea of creating multiple commits throughout the life of the project. it's something that can take some getting used to or just get forgotten. 
- What is one thing you would do differently next time you work with AI on a coding task?
  I would identify problems, and spend more time explaining the expected behavior, the actaul behavior with said bugs to give the ai more context and find better solutions.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    It really blew my mind on how much AI is capable of doing and really restructured the way in which I want to learn coding/ develop my skills for the future. 
