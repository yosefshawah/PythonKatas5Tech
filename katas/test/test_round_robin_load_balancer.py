import unittest
from katas.round_robin_load_balancer import IP, RoundRobinLoadBalancer


class TestRoundRobinLoadBalancer(unittest.TestCase):
    
    def test_ip_validation(self):
        # Valid IPs
        self.assertTrue(IP("192.168.1.1"))
        self.assertTrue(IP("0.0.0.0"))
        
        # Invalid IPs
        with self.assertRaises(ValueError):
            IP("256.1.1.1")  # > 255
        with self.assertRaises(ValueError):
            IP("192.168.1")  # Missing part
    
    def test_round_robin_routing(self):
        lb = RoundRobinLoadBalancer()
        ip1, ip2, ip3 = IP("192.168.1.1"), IP("192.168.1.2"), IP("192.168.1.3")
        
        lb.add_server(ip1)
        lb.add_server(ip2) 
        lb.add_server(ip3)
        
        # Test round robin order
        self.assertEqual(lb.route_request(), ip1)
        self.assertEqual(lb.route_request(), ip2)
        self.assertEqual(lb.route_request(), ip3)
        self.assertEqual(lb.route_request(), ip1)  # Back to first
        
        # Test server removal
        lb.remove_server(ip2)
        self.assertEqual(lb.route_request(), ip3)
        self.assertEqual(lb.route_request(), ip1)


if __name__ == "__main__":
    unittest.main()
