import random

def generate_memecoin_name():
    prefixes = ["Doge", "Shiba", "Floki", "Moon", "Fomo", "ToTheMoon"]
    suffixes = ["Coin", "Token", "Dollars", "Cash", "Cash", "Cents"]
    
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    
    return f"{prefix}{suffix}"

if __name__ == "__main__":
    print(generate_memecoin_name())
