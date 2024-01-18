from unittest.mock import patch
from main import main
import sys
sys.path.append("./")


@patch('builtins.input', side_effect=['O', '2 + 3', '*', 'O', '4 ^ 5', '*'])
def test_main(mock_input):
    main()
