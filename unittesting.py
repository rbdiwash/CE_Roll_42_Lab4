import unittest
from greed import greedy_activity_selector,recursive_acti_sel

class ActivityTest(unittest.TestCase):
	#for iterative test selection
	def test_selection(self):
		event=[[1,3,0,5,3,5,6,8,8,2,12],[4,5,6,7,9,9,10,11,12,14,16]]
		index=[1,4,8,11]
		self.assertListEqual(greedy_activity_selector(event[0],event[1]),index)
	#for recursion test selection
	def test_seL_recu(self):
		k=0
		event=[[1,3,0,5,3,5,6,8,8,2,12],[4,5,6,7,9,9,10,11,12,14,16]]
		index=[1,4,8,11]
		self.assertListEqual(greedy_activity_selector(event[0],event[1]),k,n,index)



if __name__=="__main__":
	unittest.main()

	
