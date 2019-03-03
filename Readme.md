# Python Script for Pulling Data from the Korean Public Data Portal

This is a script to request data for registered fried chicken restaurants in South Korea for my blog post. You can find the post at [here](https://yoonoh930.github.io/).

## Getting Started

### Prerequisite

In order to use the script, there should be `requests` library installed. On the terminal, install the library

```bash
pip install requests
```

In order to run the script, you have to get your own API from the [Korean Public Data Portal](https://www.data.go.kr). If you want just the data, you can use `stores.json`. After replacing `API_TOKEN` value in `credential_sample.json`, change the name of the file to `credential.json`. Then run the code in the terminal

```bash
python extracter.py
```

It will pull all the data for the registered chicken stores and save it as `stores.json`.

## License
This project is licensed under the MIT License.