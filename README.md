# crossfit-wod-api-py

A simple REST API used to learn FastAPI.

The code is based on this tutorial: <https://www.freecodecamp.org/news/rest-api-design-best-practices-build-a-rest-api/>

## How to run

Create a `Python` virtual environment and after that install the dependencies:

``` bash
pip install -r requirements.txt
```

The server should start with:

```bash
uvicorn main:app --reload
```

You will be able to make requests to: `http://127.0.0.1:8000`. If you want to change the port, run the server with the option `--port`:

```bash
uvicorn main:app --reload --port 3000
```

The API documentation will be available at: `http://127.0.0.1:8000/docs`