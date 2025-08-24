import unittest
from unittest.mock import patch, MagicMock
from katas.pinger import ping_host

class TestPinger(unittest.TestCase):
    def setUp(self):
        self.test_hostname = "test.com"
        self.test_count = 3
        
    @patch('subprocess.run')
    def test_successful_ping(self, mock_run):
        # Mock successful ping response
        mock_process = MagicMock()
        mock_process.returncode = 0
        mock_process.stdout = """
PING test.com (93.184.216.34): 56 data bytes
64 bytes from 93.184.216.34: icmp_seq=0 ttl=56 time=12.345 ms
64 bytes from 93.184.216.34: icmp_seq=1 ttl=56 time=15.678 ms
64 bytes from 93.184.216.34: icmp_seq=2 ttl=56 time=18.901 ms

--- test.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 12.345/15.641/18.901/2.678 ms
"""
        mock_run.return_value = mock_process

        result = ping_host(self.test_hostname, self.test_count)
        
        self.assertEqual(result['host'], self.test_hostname)
        self.assertAlmostEqual(result['avg_response_time_ms'], 15.641, places=3)
        self.assertTrue(result['success'])
        
        mock_run.assert_called_once_with(
            ['ping', '-c', str(self.test_count), self.test_hostname],
            capture_output=True,
            text=True,
            check=False
        )

    @patch('subprocess.run')
    def test_failed_ping(self, mock_run):
        # Mock failed ping response
        mock_process = MagicMock()
        mock_process.returncode = 1
        mock_process.stdout = ""
        mock_run.return_value = mock_process

        result = ping_host(self.test_hostname, self.test_count)
        
        self.assertEqual(result['host'], self.test_hostname)
        self.assertEqual(result['avg_response_time_ms'], 0.0)
        self.assertFalse(result['success'])

    @patch('subprocess.run')
    def test_exception_handling(self, mock_run):
        # Mock subprocess.run raising an exception
        mock_run.side_effect = Exception("Test error")

        result = ping_host(self.test_hostname, self.test_count)
        
        self.assertEqual(result['host'], self.test_hostname)
        self.assertEqual(result['avg_response_time_ms'], 0.0)
        self.assertFalse(result['success'])

if __name__ == '__main__':
    unittest.main()
