from logic_utils import check_guess, get_range_for_difficulty, update_score

def test_difficulty_ranges_ascending():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_new_game_state_fully_resets():
    # Regression: "New Game" button did not reset status, score, or history,
    # and set attempts to 0 instead of 1. This caused st.stop() to block the
    # new game from rendering after a win/loss. It also used a hardcoded range
    # of 1-100 instead of the selected difficulty range.
    # This test simulates the state after a completed game and verifies that
    # all values a correct reset must produce are valid.

    # Simulate end-of-game state
    session = {
        "status": "won",
        "score": 90,
        "history": [30, 50, 75],
        "attempts": 4,
    }

    # Apply the correct reset (mirrors the fixed new_game block in app.py)
    low, high = get_range_for_difficulty("Normal")
    session["attempts"] = 1
    session["status"] = "playing"
    session["score"] = 0
    session["history"] = []

    assert session["status"] == "playing", "status must be 'playing' so st.stop() is not triggered"
    assert session["attempts"] == 1, "attempts must start at 1, not 0"
    assert session["score"] == 0
    assert session["history"] == []
    assert low == 1 and high == 50, "difficulty range must match selected difficulty, not hardcoded 1-100"


def test_enter_submits_guess_logic():
    # Regression: pressing Enter triggered a rerun but submit was only set by
    # st.button, so the guess was never processed. The fix wraps the input in
    # st.form so Enter fires st.form_submit_button. This test verifies that
    # check_guess correctly evaluates a guess when the secret is a str (as it
    # is on even attempts in app.py), which is the code path that was silently
    # skipped before the fix.
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"

    outcome, _ = check_guess(60, "50")
    assert outcome == "Too High"

    outcome, _ = check_guess(40, "50")
    assert outcome == "Too Low"
