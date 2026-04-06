
from  .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    for ele in ingredients :
        if ele.lower() not in allowed:
            return f"{ingredients}- INVALID"
        else:
            return f"{ingredients} -VALID"
