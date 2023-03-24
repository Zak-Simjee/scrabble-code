from main import generate_letter_scores, score_word, generate_player_hand
import pytest

def test_generate_scores_is_dict():
    result = generate_letter_scores()
    assert isinstance(result, dict)

def test_word_value():
    result = score_word("GUARDIAN")
    assert result == 10

def test_lower_case_acceptance():
    result = score_word("guardian")
    assert result == 10

def test_is_string():
    with pytest.raises(TypeError) as err:
        result = score_word(5)
    assert err.value.args[0] == "Not a valid word."

def test_is_not_empty_string():
    with pytest.raises(ValueError) as err:
        result = score_word("")
    assert err.value.args[0] == "No letters found in word."


def test_player_hand_is_list():
    result = generate_player_hand()
    assert isinstance(result, list)

def test_player_hand_size_is_7():
    result = generate_player_hand()
    assert len(result) == 7

def test_player_hand_contains_letters():
    result = generate_player_hand()
    scores = generate_letter_scores()

    for i in result:
        assert i in scores
