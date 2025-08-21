import unittest
from katas.semantic_version_comparator import compare_versions


class TestSemanticVersionComparator(unittest.TestCase):
    
    def test_version1_less_than_version2(self):
        # Test cases where version1 < version2 (should return -1)
        self.assertEqual(compare_versions('1.0.0', '1.0.1'), -1)
        self.assertEqual(compare_versions('1.0.0', '1.1.0'), -1)
      
    
    def test_version1_greater_than_version2(self):
        # Test cases where version1 > version2 (should return 1)
        self.assertEqual(compare_versions('1.0.1', '1.0.0'), 1)
        self.assertEqual(compare_versions('1.1.0', '1.0.0'), 1)
       
    
    def test_versions_equal(self):
        # Test cases where version1 = version2 (should return 0)
        self.assertEqual(compare_versions('1.0.0', '1.0.0'), 0)
     
    
    def test_different_length_versions(self):
        # Test versions with different number of components
        self.assertEqual(compare_versions('1.2', '1.2.0'), 0)
        self.assertEqual(compare_versions('1.2.0', '1.2'), 0)
      
    
    def test_numeric_vs_lexicographic_comparison(self):
        # Test that comparison is numeric, not lexicographic
        # Lexicographically "10" < "2", but numerically 10 > 2
        self.assertEqual(compare_versions('1.10.0', '1.2.0'), 1)
 
    
    def test_minor_version_differences(self):
        # Test minor version when major is equal
        self.assertEqual(compare_versions('1.5.0', '1.4.99'), 1)
        self.assertEqual(compare_versions('1.4.99', '1.5.0'), -1)
        self.assertEqual(compare_versions('3.10.0', '3.9.100'), 1)
    



if __name__ == "__main__":
    unittest.main()
