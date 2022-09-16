from happytransformer import GENSettings
from happytransformer import HappyGeneration

happy_gen = HappyGeneration("GPT-NEO-1.3B", "EleutherAI/gpt-neo-1.3B")

args = GENSettings(no_repeat_ngram_size=2)
result = happy_gen.generate_text("The god of sun came to the earth to help the inca empire", args=args)
print(result.text)
top_k_sampling_settings = GENSettings(do_sample=True, early_stopping=False, top_k=50, temperature=0.7)
print(result.text)