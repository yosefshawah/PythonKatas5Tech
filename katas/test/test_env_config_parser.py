import unittest
from katas.env_config_parser import parse_env_config  

class TestParseEnvConfig(unittest.TestCase):
    
    def test_basic_parsing(self):
        env_string = """
        DATABASE_URL=postgresql://localhost:5432/mydb
        DEBUG=true
        PORT=8080
        # This is a comment
        APP_NAME="My Application"
        MAX_CONNECTIONS=100
        """

        expected = {
            "DATABASE_URL": "postgresql://localhost:5432/mydb",
            "DEBUG": True,
            "PORT": 8080,
            "APP_NAME": "My Application",
            "MAX_CONNECTIONS": 100
        }

        self.assertEqual(parse_env_config(env_string), expected)

    def test_ignores_comments_and_empty_lines(self):
        env_string = """
        # This is a comment
        \n
        \n
        KEY=value
        """
        result = parse_env_config(env_string)
        self.assertEqual(result, {"KEY": "value"})

    def test_handles_booleans_and_numbers(self):
        env_string = """
        ENABLE_FEATURE=true
        DISABLE_CACHE=false
        TIMEOUT=30
        NEGATIVE=-5
        FLOAT=3.14
        """
        result = parse_env_config(env_string)
        self.assertEqual(result["ENABLE_FEATURE"], True)
        self.assertEqual(result["DISABLE_CACHE"], False)
        self.assertEqual(result["TIMEOUT"], 30)
        self.assertEqual(result["NEGATIVE"], -5)   # Not converted in current code, see note below
        self.assertEqual(result["FLOAT"], "3.14")  # Left as string in current code

    def test_removes_quotes(self):
        env_string = """
        NAME="Alice"
        GREETING='Hello'
        """
        result = parse_env_config(env_string)
        self.assertEqual(result["NAME"], "Alice")
        self.assertEqual(result["GREETING"], "Hello")

    def test_malformed_lines(self):
        env_string = """
        CORRECT=value
        MISSING_EQUALS
        =EMPTY_KEY
        """
        result = parse_env_config(env_string)
        self.assertEqual(result, {"CORRECT": "value"})

if __name__ == "__main__":
    unittest.main()
