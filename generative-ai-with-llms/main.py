from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig

if __name__ == "__main__":
    # Loading Datasets
    huggingface_dataset_name = "knkarthick/dialogsum"
    dataset = load_dataset(huggingface_dataset_name)

    # Viewing Datasets
    example_indices = [40, 200]
    dash_line = '-'.join('' for x in range(100))
    for i, index in enumerate(example_indices):
        print(dash_line)
        print('Example ', i + 1)
        print(dash_line)
        print('INPUT DIALOGUE:')
        print(dataset['test'][index]['dialogue'])
        print(dash_line)
        print('BASELINE HUMAN SUMMARY:')
        print(dataset['test'][index]['summary'])
        print(dash_line, end='\n')

    # Loading Model
    model_name = "google/flan-t5-base"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # Loading Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

    # Test Encoding & Decoding
    sentence = "What time is it, Tom?"
    sentence_encoded = tokenizer(sentence, return_tensors="pt")
    sentence_decoded = tokenizer.decode(
        sentence_encoded["input_ids"][0],
        skip_special_tokens=True
    )
    print("ENCODED SENTENCE:\n", sentence_encoded["input_ids"][0], end="\n")
    print("DECODED SENTENCE:\n", sentence_decoded, end="\n")
