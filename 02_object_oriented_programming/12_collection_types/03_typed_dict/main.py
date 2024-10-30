from typing import TypedDict, Optional, Union

class Preferences(TypedDict):
    theme: str
    notifications: bool

class UserProfile(TypedDict):
    username: str
    email: str
    age: int
    preferences: Preferences

class ProfileUpdates(TypedDict, total=False):
    username: Optional[str]
    email: Optional[str]
    age: Optional[int]  # Ensure `age` is expected to be an int
    preferences: Optional[Preferences]

def update_user_profile(profile: UserProfile, updates: ProfileUpdates) -> UserProfile:
    for key, value in updates.items():
        if key in profile:
            profile[key] = value
        else:
            raise KeyError(f"Invalid key: {key}")
    return profile

# Correct Usage
user_profile: UserProfile = {
    "username": "MuhammadHashim",
    "email": "hashim@example.com",
    "age": 24,
    "preferences": {"theme": "dark", "notifications": True}
}

# Now if "age" is a string, mypy will detect this as an error
updates: ProfileUpdates = {"age": "twenty-five", "preferences": {"theme": "light", "notifications": False}}

updated_profile = update_user_profile(user_profile, updates)
print(updated_profile)
