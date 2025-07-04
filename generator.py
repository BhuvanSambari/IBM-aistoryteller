from transformers import pipeline, set_seed

# Use a larger model if you have enough RAM/GPU, like 'gpt2' or 'gpt2-medium'
generator = pipeline('text-generation', model='gpt2')  
set_seed(42)

def generate_story(prompt):
    result = generator(
        prompt,
        max_length=200,         # Longer output
        num_return_sequences=1,
        temperature=0.8,        # Balanced creativity
        top_p=0.9,
        do_sample=True,
        pad_token_id=50256      # Prevents warning about padding
    )
    return result[0]['generated_text']
