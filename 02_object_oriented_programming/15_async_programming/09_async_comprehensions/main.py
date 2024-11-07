import asyncio

async def fetch_user_profile(user_id):
    await asyncio.sleep(0.2)  # Simulate API call delay
    return {"id": user_id, "name": f"User{user_id}"}

async def user_id_generator():
    for uid in range(1, 6):
        await asyncio.sleep(0.1)  # Simulate data source delay
        yield uid

async def main():
    # Async List Comprehension to fetch user profiles
    user_profiles = [await fetch_user_profile(uid) async for uid in user_id_generator()]
    print("👥 User Profiles:")
    for profile in user_profiles:
        print(profile)

asyncio.run(main())