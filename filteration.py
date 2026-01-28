import numpy as np

weight = np.array ([60, 43, 90, 34, 100000000000000000000])
lbs = weight[weight > 100]
print(f"you have {lbs} pounds and diabetes")
