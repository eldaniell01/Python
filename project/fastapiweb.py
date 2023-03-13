from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()


@app.get('/')
def getList():
    return [1,2,3,4]


@app.get('/empresa')
def getList():
    return {'name': 'empresa'}

@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>"""