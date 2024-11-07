import asyncio

async def get_user_info(user_id):
    await asyncio.sleep(1)  # Simulate API call delay
    return {"id": user_id, "name": f"User{user_id}"}

async def user_info_generator(user_ids):
    for uid in user_ids:
        user_info = await get_user_info(uid)
        yield user_info

async def main():
    user_ids = [101, 102, 103]
    async for user in user_info_generator(user_ids):
        print(f"👤 Retrieved User: {user}")

asyncio.run(main())