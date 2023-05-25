## Running locally

install dependencies

```
pip install -r requirements.txt
```

Setup .env with the correct keys (see env-template)

```
cp env-template .env
# edit .env
```

Copy louis-frontend/dist into app/backend/static

Start backend:

```
flask --app app/backend/server.py --debug run
```

## Debugging in Visual Studio Code

Configuration is in ```.vscode/launch.json```

```
Run > Start Debugging
```