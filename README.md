# Extended Kalman Filter

## 1. Sensor Noise
The library Pandas in Python is used to calculate the standard deviation `\sigma` for every measurements.

```python
import pandas as pd

data = pd.read_csv(<file_name>, sep=",", header=None, skiprows=1)
print(data.std(axis=0 ))
``` 

## 2. Attitude Estimation
The Bayer Filter has two main processes, one is `Predict`, the other is `Update`. The `Update` part is already implemented by Udacity. The task for the students is to implement the `Predict` part.

* A linear complementary filter is used for this function.
* The class `Quaternion` is used for the integration.

