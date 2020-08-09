# downcast
> Reduce the pandas dataframe size automatically.

This is the test perform on [Jena dataset](https://www.kaggle.com/stytch16/jena-climate-2009-2016).

![](https://github.com/deepak7376/downcast/blob/master/src/newplot.png)

## Installation

OS X , Windows & Linux:

```sh
pip install downcast
```

## Usage example

This package is used the reduce the dataframe size without affecting the values. It find the max and min value in dataframe columns, based on these values it downcast the datatypes of that columns.

```python
from downcast import reduce
import pandas as pd

# load your dataframe
df = pd.read_csv("PATH")
# reduce the size of dataframe
df = reduce(df) 
```


## Development setup

For local development setup

```sh
git clone https://github.com/deepak7376/downcast
cd downcast
pip install -r requirements.txt
```

## Release History

* 0.0.5
    * CHANGE: work in progress

## Meta

Deepak Yadav – [@YourTwitter](https://twitter.com/dky7376) – dky.united@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/deepak7376/downcast/blob/master/LICENSE](https://github.com/deepak7376)

## Contributing

1. Fork it (<https://github.com/deepak7376/downcast/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request



