# Python





## some python code
```{code cell} ipython3
import numpy as np
import pandas as pd
data = np.random.randn(3,100)
data[0, :10]
```

<html>
    <p>output:</p>
       <img src ="https://github.com/Isha9a/yield_forecasting/blob/master/images/Sample_code1_output.png", alt = "output1" , width = "700px">
</html>


# A plot
```{code cell} ipython3
import matplotlib.pyplot as plt
plt.scatter(data[0],data[1],c=data[2], s=100*np.abs(c))
```
<html>
    <p>output:</p>
       <img src ="https://github.com/Isha9a/yield_forecasting/blob/master/images/Sample_code2_output.png", alt = "output2" , width = "500px">
</html>

