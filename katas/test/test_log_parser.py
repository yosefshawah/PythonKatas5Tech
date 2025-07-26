import unittest
from katas.fastapi_log_parser import parse_fastapi_log  

class TestParseFastAPILog(unittest.TestCase):

    def test_valid_log_get(self):
        log = 'INFO:     127.0.0.1:54321 - "GET /api/users HTTP/1.1" 200 OK'
        expected = {
            "client_ip": "127.0.0.1",
            "client_port": "54321",
            "http_method": "GET",
            "endpoint": "/api/users",
            "http_version": "1.1",
            "status_code": "200",
            "status_text": "OK"
        }
        self.assertEqual(parse_fastapi_log(log), expected)

    def test_valid_log_post(self):
        log = 'INFO:     192.168.1.100:45678 - "POST /api/auth/login HTTP/1.1" 401 Unauthorized'
        result = parse_fastapi_log(log)
        self.assertEqual(result["http_method"], "POST")
        self.assertEqual(result["endpoint"], "/api/auth/login")
        self.assertEqual(result["status_code"], "401")

    def test_valid_log_with_spaces_in_status(self):
        log = 'INFO:     172.16.0.1:8080 - "GET /health HTTP/1.1" 500 Internal Server Error'
        result = parse_fastapi_log(log)
        self.assertEqual(result["status_text"], "Internal Server Error")

    def test_malformed_log_returns_empty(self):
        log = 'Malformed log line without expected format'
        self.assertEqual(parse_fastapi_log(log), {})

    def test_empty_string(self):
        self.assertEqual(parse_fastapi_log(""), {})

    def test_extra_spaces(self):
        log = 'INFO:     10.0.0.5:33333 - "PUT    /api/users/123   HTTP/1.1"    200    OK'
        expected = {
            "client_ip": "10.0.0.5",
            "client_port": "33333",
            "http_method": "PUT",
            "endpoint": "/api/users/123",
            "http_version": "1.1",
            "status_code": "200",
            "status_text": "OK"
        }
        self.assertEqual(parse_fastapi_log(log), expected)


if __name__ == '__main__':
    unittest.main()
