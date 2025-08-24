import unittest
from unittest.mock import patch, MagicMock
from katas.system_resource_monitor import get_cpu_usage, get_memory_usage, get_disk_usage

class TestSystemResourceMonitor(unittest.TestCase):
    def setUp(self):
        # Common test values
        self.gb_factor = 1024 ** 3
        
    @patch('psutil.cpu_percent')
    @patch('psutil.cpu_count')
    def test_get_cpu_usage(self, mock_cpu_count, mock_cpu_percent):
        # Mock CPU information
        mock_cpu_count.return_value = 4
        mock_cpu_percent.side_effect = [75.5, [70.0, 80.0, 75.0, 77.0]]
        
        result = get_cpu_usage()
        
        self.assertEqual(result['core_count'], 4)
        self.assertEqual(result['usage_percent'], 75.5)
        self.assertEqual(result['per_core_usage'], [70.0, 80.0, 75.0, 77.0])
        
        # Verify correct calls
        mock_cpu_count.assert_called_once()
        self.assertEqual(mock_cpu_percent.call_count, 2)

    @patch('psutil.virtual_memory')
    def test_get_memory_usage(self, mock_virtual_memory):
        # Mock memory information
        mock_memory = MagicMock()
        mock_memory.total = 16 * self.gb_factor  # 16 GB total
        mock_memory.available = 8 * self.gb_factor  # 8 GB available
        mock_virtual_memory.return_value = mock_memory
        
        result = get_memory_usage()
        
        self.assertEqual(result['total_gb'], 16)
        self.assertEqual(result['available_gb'], 8)
        self.assertEqual(result['used_gb'], 8)  # 16 GB - 8 GB = 8 GB used
        
        mock_virtual_memory.assert_called_once()

    @patch('psutil.disk_usage')
    def test_get_disk_usage(self, mock_disk_usage):
        # Mock disk information
        mock_disk = MagicMock()
        mock_disk.total = 500 * self.gb_factor  # 500 GB total
        mock_disk.used = 300 * self.gb_factor   # 300 GB used
        mock_disk.free = 200 * self.gb_factor   # 200 GB free
        mock_disk.percent = 60.0                # 60% used
        mock_disk_usage.return_value = mock_disk
        
        result = get_disk_usage("/")
        
        self.assertEqual(result['total_gb'], 500)
        self.assertEqual(result['used_gb'], 300)
        self.assertEqual(result['free_gb'], 200)
        self.assertEqual(result['usage_percent'], 60.0)
        
        mock_disk_usage.assert_called_once_with("/")

    @patch('psutil.disk_usage')
    def test_get_disk_usage_custom_path(self, mock_disk_usage):
        # Test with custom path
        mock_disk = MagicMock()
        mock_disk.total = 100 * self.gb_factor
        mock_disk.used = 50 * self.gb_factor
        mock_disk.free = 50 * self.gb_factor
        mock_disk.percent = 50.0
        mock_disk_usage.return_value = mock_disk
        
        custom_path = "/home"
        result = get_disk_usage(custom_path)
        
        mock_disk_usage.assert_called_once_with(custom_path)

if __name__ == '__main__':
    unittest.main()
