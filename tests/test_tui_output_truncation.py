import pytest
from openhands_cli.tui.tui import truncate_output, MAX_OUTPUT_LINES


class TestTruncateOutput:
    """Test suite for the truncate_output function."""

    def test_short_output_not_truncated(self):
        """Output with fewer lines than max should not be truncated."""
        short_output = "\n".join([f"Line {i}" for i in range(5)])
        
        result, was_truncated = truncate_output(short_output)
        
        assert result == short_output
        assert was_truncated is False