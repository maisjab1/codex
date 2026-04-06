

def validate_ingredients(ingredients: str) -> str:
    from  .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    for ele in ingredients :
        if ele.lower() not in allowed:
            return f"{ingredients}- INVALID"
        else:
            return f"{ingredients} -VALID"
