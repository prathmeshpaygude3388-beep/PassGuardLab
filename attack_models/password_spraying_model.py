SPRAY_PASSWORDS = [
    "Welcome@123", "Company@123",
    "Spring@2024", "Winter@2024",
    "Password@123"
]

def password_spraying_attack(password: str):
    hit = password in SPRAY_PASSWORDS

    return {
        "attack": "Password Spraying",
        "risk_score": 0.95 if hit else 0.25,
        "confidence": 0.9,
        "details": {
            "matched_common_password": hit,
            "spray_list_size": len(SPRAY_PASSWORDS)
        },
        "recommendation": "Block seasonal and organizational passwords"
    }
