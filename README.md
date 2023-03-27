# json_flatten_py
json_flatten_py is a Python library for flattening complex JSONs.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install json_flatten_py
```

## Usage

```python
from from simple_flatten_json_py import flatten_json

# Sample JSON data
data={
  "cat": [
    {
      "fish": "tuna"
    },
    {
      "chicken": 3
    },
    {
      "medicine": {
        "pills": 20
      }
    }
  ]
}
# returns a flattened json 
# {"_cat_0_fish": "tuna",  "_cat_1_chicken": 3,"_cat_2_medicine_pills": 20}
'''
print(flatten_json.flatten_json(data))
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
