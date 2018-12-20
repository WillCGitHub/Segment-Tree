import sys

class SegmentTreeNode:
	def __init__(self, start, end, min_val, max_val):
		self.start, self.end = start, end
		self.min_val, self.max_val = min_val, max_val
		self.left, self.right = None, None

	def __repr__(self, ):
		return "[{}, {}, min={}, max={}]".format(self.start, self.end, self.min_val, self.max_val)


class SegmentTree:
	def __init__(self, arr):
		start, end = 0, len(arr) - 1
		self.root = self._build_tree(start, end, arr)

	def _build_tree(self, start, end, arr):
		if start > end:
			return

		if start == end:
			return SegmentTreeNode(start, end, arr[start], arr[start])

		mid = (start + end) // 2
		node = SegmentTreeNode(start, end, arr[start], arr[start])
		node.left = self._build_tree(start, mid, arr)
		node.right = self._build_tree(mid + 1, end, arr)
		if node.left:
			node.max_val = max(node.max_val, node.left.max_val)
			node.min_val = min(node.min_val, node.left.min_val)
		if node.right:
			node.max_val = max(node.max_val, node.right.max_val)
			node.min_val = min(node.min_val, node.right.min_val)

		return node

	def query_min(self, start, end, root):
		return self.query(start, end, root, min)

	def query_max(self, start, end, root):
		return self.query(start, end, root, max)

	def query(self, start, end, root, comp_func):
		if comp_func(0, 1) == 0:
			# query min
			ans = sys.maxsize
			return_val = root.min_val
		else:
			# query max
			ans = -sys.maxsize
			return_val = root.max_val

		if start <= root.start and root.end <= end:
			return return_val

		mid = (root.start + root.end) // 2
		
		if mid >= start:
			ans = comp_func(ans, self.query(start, end, root.left, comp_func))
		if mid + 1 <= end:
			ans = comp_func(ans, self.query(start, end, root.right, comp_func))

		return ans

	def query_sum(self, start, end, root):
		if start <= root.start and root.end <= end:
			if not root.left and not root.right:
				return root.max_val

		ans = 0
		mid = (root.start + root.end) // 2
		if start <= mid:
			ans  += self.query_sum(start, end, root.left)

		if mid + 1 <= end:
			ans += self.query_sum(start, end, root.right)

		return ans


	def modify(self, root, index, value):
		if root.start == root.end and root.start == index:
			root.max_val = value
			root.min_val = value
			return

		mid = (root.start + root.end) // 2
		if index <= mid:
			self.modify(root.left, index, value)
			root.max_val = max(root.left.max_val, root.right.max_val)
			root.min_val = min(root.left.min_val, root.right.min_val)
		else:
			self.modify(root.right, index, value)
			root.max_val = max(root.left.max_val, root.right.max_val)
			root.min_val = min(root.left.min_val, root.right.min_val)

		return