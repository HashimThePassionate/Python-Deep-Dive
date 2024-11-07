# tcp_echo_server.py
import asyncio

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info('peername')
    print(f"👤 New connection from {addr}")
    try:
        while True:
            data = await reader.readline()
            if not data:
                print(f"🔌 Connection closed by {addr}")
                break
            message = data.decode().strip()
            print(f"💬 Received from {addr}: {message}")
            response = message.upper() + '\n'
            writer.write(response.encode())
            await writer.drain()
    except asyncio.CancelledError:
        print(f"🚨 Connection with {addr} is being closed gracefully.")
        writer.close()
        await writer.wait_closed()
        raise
    except Exception as e:
        print(f"❌ Error with {addr}: {e}")
    finally:
        print(f"🔒 Connection with {addr} has been closed.")

async def main(host='127.0.0.1', port=8888):
    server = await asyncio.start_server(handle_client, host, port)
    addr = server.sockets[0].getsockname()
    print(f"🚀 Serving on {addr}")
    
    async with server:
        try:
            await server.serve_forever()
        except asyncio.CancelledError:
            print("🛑 Server is shutting down...")
            server.close()
            await server.wait_closed()
            tasks = [task for task in asyncio.all_tasks() if task is not asyncio.current_task()]
            print(f"📋 Cancelling {len(tasks)} active tasks...")
            for task in tasks:
                task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
            print("✅ Shutdown complete.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("✋ Received exit signal. Exiting gracefully...")
