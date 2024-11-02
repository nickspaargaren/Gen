from utils import create_safe_filename


def test_create_safe_filename_short_prompt():
    prompt = "short_test_filename"
    result = create_safe_filename(prompt)
    assert result == "short_test_filename", "Short prompt should not change."


def test_create_safe_filename_long_prompt():
    prompt = "a" * 60  # A string longer than 50 characters
    result = create_safe_filename(prompt)
    assert (
        result == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa_13d956033d"
    ), "Long prompt should be truncated with an hash."
