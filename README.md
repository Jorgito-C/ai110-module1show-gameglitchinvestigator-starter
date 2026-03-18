# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

### Game Purpose

This is a number guessing game where the player tries to guess a secret number within a limited number of attempts. The difficulty setting changes the range of possible numbers and how many attempts you get. After each guess, the game gives you a hint telling you to go higher or lower until you either win or run out of attempts.

### Bugs Found

1. **Hints were backwards** — guessing too high showed "Go HIGHER" and guessing too low showed "Go LOWER". The comparison logic was returning the wrong outcome for each case.
2. **Normal and Hard difficulty ranges were swapped** — Normal had a range of 1–100 and Hard had 1–50. They should be the opposite since Hard should be harder.
3. **Changing difficulty didn't affect the game** — the secret number was generated once and never updated when the difficulty changed. Clicking New Game also ignored the selected difficulty and always used `randint(1, 100)`.
4. **New Game didn't fully reset** — after losing, clicking New Game left the `status` as `"lost"` and kept the old guess history, so the game was immediately blocked by `st.stop()`.
5. **Game started with 1 attempt already used** — attempts initialized to 1 instead of 0, making it look like one guess was used before the player did anything.
6. **Submitting a guess required two clicks** — typing a new guess and clicking Submit once was not enough because Streamlit fired two separate reruns, losing the button click on the first one.
7. **Even-numbered attempts used broken string comparison** — the secret was cast to a string on every even attempt, so comparisons like `"7" > "50"` returned the wrong result due to lexicographic ordering.
8. **`logic_utils.py` functions were never implemented** — all four functions just raised `NotImplementedError`, and `app.py` never imported from the file either.
9. **Tests had wrong assertions** — `check_guess` returns a tuple `(outcome, message)` but the tests compared the result directly to a plain string, so they would always fail.
10. **Attempt limits were out of order** — Easy gave 6 attempts and Normal gave 8, meaning Easy was actually harder than Normal.

### Fixes Applied

1. Swapped the hint messages so "Too High" returns "Go LOWER" and "Too Low" returns "Go HIGHER".
2. Swapped the difficulty ranges so Normal is 1–50 and Hard is 1–100.
3. Added difficulty change detection in session state — if the dropdown changes, the secret, attempts, status, and history all reset.
4. Fixed the New Game button to also reset `status` and `history`, and to use `randint(low, high)` based on the current difficulty.
5. Changed all attempts initialization from 1 to 0 so the counter starts correctly.
6. Wrapped the text input and Submit button in a `st.form` so both are batched into one rerun on submit.
7. Removed the even-attempt string cast and always compare the guess against the integer secret.
8. Implemented all four functions in `logic_utils.py` and updated `app.py` to import from it.
9. Fixed the test assertions to unpack the tuple: `outcome, message = check_guess(...)`.
10. Updated attempt limits to Easy: 8, Normal: 6, Hard: 5 so harder difficulties give fewer attempts.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
