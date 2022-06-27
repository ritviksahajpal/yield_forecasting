---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Sample Code

```{code-cell} ipython3
import numpy as np
import pandas as pd
data = np.random.randn(3,100)
data[0, :10]
```

```{code-cell} ipython3
##PLOT
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
plt.scatter(data[0],data[1],c=data[2], s=100*np.abs(data[2]))
```

```{code-cell} ipython3

```
