import unittest
import SegmentTree
from random import randint
import sys

class TestSegmentTree(unittest.TestCase):
	def test_query(self):
		nums = []
		for i in range(100):
			nums.append(randint(-10000, 10000))

		st = SegmentTree.SegmentTree(nums)
		root = st.root

		randint1 = randint(0, 99)
		randint2 = randint(0, 99)
		if randint1 > randint2:
			randint1, randint2 = randint2, randint1
		
		interval = (randint1, randint2)

		min_ans = st.query_min(interval[0], interval[1], root)
		min_solution = min(nums[interval[0]:interval[1] + 1])
		max_ans = st.query_max(interval[0], interval[1], root)
		max_solution = max(nums[interval[0]:interval[1] + 1])
		sum_ans = st.query_sum(0, 99, root)
		self.assertEqual(min_ans, min_solution)
		self.assertEqual(max_ans, max_solution)
		self.assertEqual(sum(nums), sum_ans)
		print("Query pass")

	def test_modify(self):
		nums = []
		for i in range(100):
			nums.append(randint(-10000, 10000))


		st = SegmentTree.SegmentTree(nums)
		root = st.root

		randint1 = randint(0, 99)
		st.modify(root, randint1, -sys.maxsize)
		min_ans = st.query_min(0, 99, root)

		self.assertEqual(min_ans, -sys.maxsize)

		st.modify(root, randint1, sys.maxsize)
		max_ans = st.query_max(0, 99, root)
		self.assertEqual(max_ans, sys.maxsize)

		print("modify pass")



if __name__ == '__main__':
	unittest.main()