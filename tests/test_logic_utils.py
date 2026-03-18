from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score


# --- get_range_for_difficulty ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100


# --- parse_guess ---

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_valid_decimal():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None

def test_parse_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."


# --- check_guess ---

def test_correct_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(10, 50)
    assert outcome == "Too Low"

def test_hint_message_correct():
    outcome, message = check_guess(50, 50)
    assert "Correct" in message

def test_hint_message_lower():
    outcome, message = check_guess(99, 10)
    assert "LOWER" in message

def test_hint_message_higher():
    outcome, message = check_guess(1, 90)
    assert "HIGHER" in message


# --- update_score ---

def test_win_on_first_attempt():
    # attempt_number=1, points = 100 - 10*(1+1) = 80
    new_score = update_score(0, "Win", 1)
    assert new_score == 80

def test_win_minimum_points():
    # attempt_number=10, points would be negative, should floor at 10
    new_score = update_score(0, "Win", 10)
    assert new_score == 10

def test_too_high_deducts_points():
    new_score = update_score(100, "Too High", 1)
    assert new_score == 95

def test_too_low_deducts_points():
    new_score = update_score(100, "Too Low", 1)
    assert new_score == 95

def test_unknown_outcome_unchanged():
    new_score = update_score(100, "Unknown", 1)
    assert new_score == 100
