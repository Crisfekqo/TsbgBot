def spin_character():
    roll = random.uniform(0, 100)
    cumulative = 0
    for rarity, chance in RARITY_POOL:
        cumulative += chance
        if roll <= cumulative:
            character = random.choice(CHARACTERS[rarity])
            return f"🎰 You spun... {rarity}!\n✨ **{character}** is yours!"
    
    # If somehow no match (edge case), return Common by default
    character = random.choice(CHARACTERS["⚪️ Common"])
    return f"🎰 You spun... ⚪️ Common!\n✨ **{character}** is yours!"
