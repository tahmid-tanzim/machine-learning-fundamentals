from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig


class SummarizeDialogue:
    def __init__(self, model_name="google/flan-t5-base", dataset_name=None):
        # Loading Datasets
        huggingface_dataset_name = "knkarthick/dialogsum"
        self.dataset = load_dataset(dataset_name or huggingface_dataset_name)

        # Loading Model
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

        # Loading Tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

    def view_dataset(self):
        # Viewing Datasets
        example_indices = [40, 200]
        dash_line = '-'.join('' for x in range(100))
        for i, index in enumerate(example_indices):
            print(dash_line)
            print('Example ', i + 1)
            print(dash_line)
            print('INPUT DIALOGUE:')
            print(self.dataset['test'][index]['dialogue'])
            print(dash_line)
            print('BASELINE HUMAN SUMMARY:')
            print(self.dataset['test'][index]['summary'])
            print(dash_line, end='\n')

    def test_encoding_decoding(self, sentence="What time is it, Tom?"):
        # Test Encoding & Decoding
        sentence_encoded = self.tokenizer(sentence, return_tensors="pt")
        sentence_decoded = self.tokenizer.decode(
            sentence_encoded["input_ids"][0],
            skip_special_tokens=True
        )
        print("ENCODED SENTENCE:\n", sentence_encoded["input_ids"][0], end="\n")
        print("DECODED SENTENCE:\n", sentence_decoded, end="\n")


if __name__ == "__main__":
    dialogue = SummarizeDialogue()
    dialogue.test_encoding_decoding("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")

