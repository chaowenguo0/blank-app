import asyncio, aiohttp.web, math, pathlib, uvloop, os

async def main():
    app = aiohttp.web.Application()
    app.add_routes([aiohttp.web.static('/', pathlib.Path(__file__).resolve().parent, show_index=True)])
    runner = aiohttp.web.AppRunner(app)
    await runner.setup()
    site = aiohttp.web.TCPSite(runner, host='127.0.0.1' ,port=8501)
    await site.start()
    await asyncio.sleep(math.inf)

uvloop.run(main())
