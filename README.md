# Extended Kalman Filter

## 1. Sensor Noise
The library Pandas in Python is used to calculate the standard deviation `\sigma` for every measurements.

```python
import pandas as pd

data = pd.read_csv(<file_name>, sep=",", header=None, skiprows=1)
print(data.std(axis=0 ))
``` 