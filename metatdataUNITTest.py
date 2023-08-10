import unittest
from unittest.mock import patch
from metadatafinal import extract_metadata  # Import the function you want to test

class TestMetadataExtraction(unittest.TestCase):
    @patch('subprocess.check_output')  # Mock the subprocess.check_output function
    def test_extract_metadata(self, mock_check_output):
        # Simulate the behavior of subprocess.check_output() with a mock
        mock_check_output.return_value = b"Sample metadata content"

        # Simulate a call to extract_metadata()
        test_file_path = "test_file.txt"
        expected_output = "Sample metadata content"
        actual_output = extract_metadata(test_file_path)

        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
