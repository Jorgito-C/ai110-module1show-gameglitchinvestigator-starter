# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").

If i guessed a number that was too high, the message said "GO HIGHER".
Another thing i noticed was that the "normal" difficulty had a range of 1 to 100, whereas "hard" difficulty had a rnage of 1to 50. They should be switched.
A third thing I noticed was that when i changed the difficulty level in the dropdowbn menu, it would not change the actual game. For example i chose "easy" which should be a number from range 1 to 20. I even clicked on new game and would get numbers higher than 20 and even higher than 50.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code in terminal and also Copilot inline chat. 
One example of a suggestion that was correct was changing the session state to account for the difficulty level. st.session_state.secret = random.randint(1, 100) ->  st.session_state.secret = random.randint(low, high)  
 One example of a suggestion that was misleading is for the attempts allowed for each difficulty, "easy" gave 6 attempts, "normal" gave 8, and "hard" only 5. Easy and normal should just be switched, but Claude just kept "normal" difficulty as 8 and made "easy" give 10 attempts. 


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I ran the app again and made sure the outcome was different and correct. I also ran pytest on the test file in the tests/ folder, which tested all four logic functions — get_range_for_difficulty, parse_guess, check_guess, and update_score. The tests caught that check_guess returns a tuple, not a plain string, which meant the original assertions were never actually verifying anything correctly. Claude Code helped design the tests by identifying edge cases to cover, like decimal inputs, empty strings, and the minimum score floor on a win.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret kept changing because every time I clicked a button or typed something, Streamlit re-ran the entire app.py file from top to bottom, which called random.randint() again and generated a new number every time. Streamlit reruns are like refreshing a webpage — everything resets unless you save it somewhere persistent. Session state is like a sticky notepad that survives each refresh, so anything stored there stays the same across reruns. The fix was wrapping the secret generation in a check: only generate a new secret if one doesn't already exist in session state, so it gets created once and stays stable for the whole game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is running the app manually after every fix to verify the behavior actually changed, not just that the code looks right. Next time I work with AI on a coding task, I would test each suggestion in the running app before accepting it, rather than trusting the explanation alone. This project showed me that AI-generated code can look polished and complete while hiding subtle logic bugs — like swapped difficulty ranges or broken comparisons — that only show up when you actually play the game.
