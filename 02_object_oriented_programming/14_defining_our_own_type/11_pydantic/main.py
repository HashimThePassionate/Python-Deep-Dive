from pydantic import BaseModel, EmailStr, Field, validator

class User(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    age: int = Field(..., ge=0, le=120)  # age >= 0 and <= 120
    phone: str

    @validator('phone')
    def phone_must_be_digits(cls, v):
        if not v.isdigit():
            raise ValueError('Phone number must contain only digits.')
        if len(v) != 10:
            raise ValueError('Phone number must be exactly 10 digits.')
        return v
    
def main():
    try:
        user = User(
            name="Ali Ahmed",
            email="ali@example.com",
            age=30,
            phone="1234567890"
        )
        print(user)
    except ValidationError as e:
        print(e.json())

if __name__ == "__main__":
        main()