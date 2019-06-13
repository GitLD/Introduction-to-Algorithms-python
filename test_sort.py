import unittest

import sort

class TestSort(unittest.TestCase):
	# Test Insertion Sort
	def test_insertion_sort(self):
		# 断言空列表直接返回
		self.assertEqual(sort.insertion_sort([]), [])
		# 断言单元素列表直接返回
		self.assertEqual(sort.insertion_sort([1]), [1])
		# 断言2元素列表
		self.assertEqual(sort.insertion_sort([2, 1]), [1, 2])
		# 断言3元素列表
		self.assertEqual(sort.insertion_sort([1, 3, 2]), [1, 2, 3])
		
		