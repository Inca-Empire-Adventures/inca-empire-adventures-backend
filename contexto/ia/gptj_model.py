from happytransformer import GENSettings
from happytransformer import HappyGeneration

happy_gen = HappyGeneration("GPT-NEO-1.3B", "EleutherAI/gpt-neo-1.3B")

args = GENSettings(no_repeat_ngram_size=2)
result = happy_gen.generate_text("The god of sun came to the earth to help the inca empire", args=args)
print(result.text)