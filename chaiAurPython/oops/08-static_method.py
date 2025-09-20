class ChaiUtils:
    
    @staticmethod
    def clean_ingedients(text):
        return [i.strip() for i in text.split(",")]

raw = "  water, elychi, some suger"

obj = ChaiUtils()

print(obj.clean_ingedients(raw))
print(ChaiUtils.clean_ingedients(raw))