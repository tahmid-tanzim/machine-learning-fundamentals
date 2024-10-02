from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig


class SummarizeDialogue:
    example_indices = [40, 200]
    dash_line = '-'.join('' for x in range(100))

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
        for i, index in enumerate(self.example_indices):
            print(self.dash_line)
            print('Example ', i + 1)
            print(self.dash_line)
            print('INPUT DIALOGUE:\n', self.dataset['test'][index]['dialogue'], end='\n')
            print(self.dash_line)
            print('BASELINE HUMAN SUMMARY:\n', self.dataset['test'][index]['summary'], end='\n')
            print(self.dash_line, end='\n')

    def test_encoding_decoding(self, sentence="What time is it, Tom?"):
        # Test Encoding & Decoding
        sentence_encoded = self.tokenizer(sentence, return_tensors="pt")
        sentence_decoded = self.tokenizer.decode(
            sentence_encoded["input_ids"][0],
            skip_special_tokens=True
        )
        print("ENCODED SENTENCE:\n", sentence_encoded["input_ids"][0], end="\n")
        print("DECODED SENTENCE:\n", sentence_decoded, end="\n")

    def summarize_dialogue_without_prompt_engineering(self):
        for i, index in enumerate(self.example_indices):
            dialogue = self.dataset['test'][index]['dialogue']
            summary = self.dataset['test'][index]['summary']
            encoded_dialogue = self.tokenizer(dialogue, return_tensors="pt")
            decoded_dialogue = self.tokenizer.decode(
                self.model.generate(
                    encoded_dialogue["input_ids"],
                    max_new_tokens=50,
                )[0],
                skip_special_tokens=True
            )
            print(self.dash_line)
            print('Example ', i + 1)
            print(self.dash_line)
            print('INPUT PROMPT:\n', dialogue, end='\n')
            print(self.dash_line)
            print('BASELINE HUMAN SUMMARY:\n', summary, end='\n')
            print('MODEL GENERATION - WITHOUT PROMPT ENGINEERING:\n', decoded_dialogue, end='\n')

    def summarize_dialogue_with_zero_shot_inference(self):
        for i, index in enumerate(self.example_indices):
            dialogue = self.dataset['test'][index]['dialogue']
            summary = self.dataset['test'][index]['summary']

            prompt = f"Summarize the following conversation.\n{dialogue}\nSummary:\n"

            encoded_dialogue = self.tokenizer(prompt, return_tensors="pt")
            decoded_dialogue = self.tokenizer.decode(
                self.model.generate(
                    encoded_dialogue["input_ids"],
                    max_new_tokens=50,
                )[0],
                skip_special_tokens=True
            )
            print(self.dash_line)
            print('Example ', i + 1)
            print(self.dash_line)
            print('INPUT PROMPT:\n', prompt, end='\n')
            print(self.dash_line)
            print('BASELINE HUMAN SUMMARY:', summary, end='\n')
            print('MODEL GENERATION - ZERO SHOT:', decoded_dialogue, end='\n')


if __name__ == "__main__":
    sd = SummarizeDialogue()
    # sd.view_dataset()
    sd.summarize_dialogue_without_prompt_engineering()
    sd.summarize_dialogue_with_zero_shot_inference()
