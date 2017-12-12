import numpy as np
def test_run():
    np.random.seed(100)
    a = np.random.randint(0,10,size=(5,4))
    print "Array:\n", a
    print "Minimum in each row: \n",a.min(axis=0)
    print "Maximum in each row: \n",a.max(axis=1)
    print "Mean of all elements: \n",a.mean()

test_run()
