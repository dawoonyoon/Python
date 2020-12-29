import sys
import mod2

print(sys.path)

sys.path.append('./../myModule3')
print('\n\n,sys.path')

import mod3

print('\n\n',mod3.sum(10,20))
