from typing import TypedDict

class Preferences(TypedDict):
    theme: str
    notifications: bool

class UserProfile(TypedDict):
    username: str
    email: str
    age: int
    preferences: Preferences


class ProfileUpdates(TypedDict, total=False):
    username: str | None
    email: str | None
    age: int | None 
    preferences: Preferences | None


def update_user_profile(profile: UserProfile, updates: ProfileUpdates) -> UserProfile:
    if "username" in updates and updates["username"] is not None:
        profile["username"] = updates["username"]
    if "email" in updates and updates["email"] is not None:
        profile["email"] = updates["email"]
    if "age" in updates and updates["age"] is not None:
        profile["age"] = updates["age"]
    if "preferences" in updates and updates["preferences"] is not None:
        profile["preferences"] = updates["preferences"]
    
    return profile

# Define a correct user profile
user_profile: UserProfile = {
    "username": "MuhammadHashim",
    "email": "hashim@example.com",
    "age": 24,
    "preferences": {"theme": "dark", "notifications": True}
}

# Define updates with an incorrect type for `age`
updates: ProfileUpdates = {"age": 25, "preferences": {"theme": "light", "notifications": False}}

# Apply updates (mypy will flag this as an error due to incorrect type for `age`)
updated_profile = update_user_profile(user_profile, updates)
print(updated_profile)
