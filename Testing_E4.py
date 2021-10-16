import logged_in
import ui
import login_main
import pytest


def test_1(capsys):
    input_values = [2, "John", "9^rNeC232*", "John", "Johnson", 1, "John", "9^rNeC232*", 4, 5, 1]

    def mock_input(s):
        return input_values.pop(0)

    Login.input = mock_input

    with pytest.raises(SystemExit):
        Login.main()

    out, err = capsys.readouterr()