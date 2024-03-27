from fastapi import FastAPI

app = FastAPI(
    title='TradeOverseer'
)

@app.get(f'/', tags=['Setup'])
async def get_root_handler():
    return 'Hello, world!'

