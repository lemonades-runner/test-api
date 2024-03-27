from fastapi import FastAPI

app = FastAPI(
    title='Test API to run on GitHub'
)


@app.get(f'/', tags=['Setup'])
async def get_root_handler():
    return 'Hello, world!'


@app.get(f'/readyz', tags=['Setup'])
async def get_readyz_handler():
    return 'ready'


@app.get(f'/healthz', tags=['Setup'])
async def get_healthz_handler():
    return 'health'
