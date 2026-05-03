# Create data using the dataframe
import pandas as pd
data={'Name':['Krish','Johan','Jack'],
      'Age':[25,30,45],
      'City':['Bangalore','New york','Florida']
}
df=pd.DataFrame(data)
print(df)
