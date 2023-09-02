def test_write_file(tmp_path):
    """Test write_file()"""
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."

def test_append_file(tmp_path):
    """Test append_file()"""

    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    append_content = "\nAppended content."

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return None  # Return None to indicate that the file was not found
