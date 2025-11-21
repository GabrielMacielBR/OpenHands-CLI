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
    
    def test_long_output_truncated(self):
        """Output with more lines than max should be truncated."""
        long_output = "\n".join([f"Line {i}" for i in range(20)])
        
        result, was_truncated = truncate_output(long_output)
        
        result_lines = result.splitlines()
        assert len(result_lines) == MAX_OUTPUT_LINES + 1
        assert was_truncated is True
        assert "more lines" in result
    
    def test_shows_correct_hidden_line_count(self):
        """Truncation message should show how many lines were hidden."""
        output = "\n".join([f"Line {i}" for i in range(100)])
        
        result, was_truncated = truncate_output(output)
        
        assert "85" in result  
        assert was_truncated is True
    
    def test_message_instructs_how_to_view_full(self):
        """Truncation message should tell user how to see full output."""
        output = "\n".join([f"Line {i}" for i in range(50)])
        
        result, was_truncated = truncate_output(output)
        
        assert "/full" in result.lower()  # Deve mencionar comando /full
        assert was_truncated is True