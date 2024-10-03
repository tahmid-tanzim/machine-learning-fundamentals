import random

from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig


class SummarizeDialogue:
    test_data_indices = [40, 220]
    type_indices = {
        "test": {
            "transportation": [
                4,
                40,
                481,
                482
            ],
            "job application": [
                219,
                220
            ]
        },
        "train": {
            "transportation": [
                710,
                1492,
                2852,
                5074,
                6955,
                9358,
                9417,
                10062,
                10690,
                11359,
                11395,
                11404
            ],
            "job application": [
                7,
                1014,
                2461,
                2697,
                3752,
                4624,
                4685,
                7173,
                7413,
                7859,
                8353,
                8991,
                9379,
                10472,
                10847
            ]
        }
    }

    dash_line = "-".join("" for x in range(100))

    def __init__(self, model_name="google/flan-t5-base", dataset_name=None):
        # Loading Datasets
        huggingface_dataset_name = "knkarthick/dialogsum"
        self.dataset = load_dataset(dataset_name or huggingface_dataset_name)

        # Loading Model
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

        # Loading Tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

    def view_dataset(self, dataset_type="test"):
        # Viewing Datasets
        for i, index in enumerate(self.test_data_indices):
            print(self.dash_line)
            print("Example ", i + 1)
            print(self.dash_line)
            print("ID:\n", self.dataset[dataset_type][index]["id"], end="\n")
            print(self.dash_line)
            print("DIALOGUE:\n", self.dataset[dataset_type][index]["dialogue"], end="\n")
            print(self.dash_line)
            print("SUMMARY:\n", self.dataset[dataset_type][index]["summary"], end="\n")
            print(self.dash_line)
            print("TOPIC:\n", self.dataset[dataset_type][index]["topic"], end="\n")
            print(self.dash_line, end="\n")

    def explore_dataset_by_type(self, topic, dataset_type="train"):
        # Viewing Datasets
        count = 20
        print(self.dash_line)
        print("Explore Dataset Type:", dataset_type)
        index = 0
        for item in self.dataset[dataset_type]:
            if count <= 0:
                break
            elif item["topic"] == topic:
                print(self.dash_line)
                print("INDEX:\n", index, end="\n")
                print(self.dash_line)
                print("ID:\n", item["id"], end="\n")
                print(self.dash_line)
                print("DIALOGUE:\n", item["dialogue"], end="\n")
                print(self.dash_line)
                print("SUMMARY:\n", item["summary"], end="\n")
                print(self.dash_line)
                print("TOPIC:\n", item["topic"], end="\n")
                print(self.dash_line, end="\n")
                count -= 1
            index += 1

    def get_random_type_indices(self, dataset_type: str, topic: str, max_size: int = 0) -> set:
        if max_size <= 0 or len(self.type_indices[dataset_type][topic]) < max_size:
            return set()
        return set(random.choices(population=self.type_indices[dataset_type][topic], k=max_size))

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
        for i, index in enumerate(self.test_data_indices):
            dialogue = self.dataset["test"][index]["dialogue"]
            summary = self.dataset["test"][index]["summary"]
            encoded_dialogue = self.tokenizer(dialogue, return_tensors="pt")
            decoded_dialogue = self.tokenizer.decode(
                self.model.generate(
                    encoded_dialogue["input_ids"],
                    max_new_tokens=50,
                )[0],
                skip_special_tokens=True
            )
            print(self.dash_line)
            print("Example ", i + 1)
            print(self.dash_line)
            print("INPUT PROMPT:\n", dialogue, end="\n")
            print(self.dash_line)
            print("BASELINE HUMAN SUMMARY:\n", summary, end="\n")
            print("MODEL GENERATION - WITHOUT PROMPT ENGINEERING:\n", decoded_dialogue, end="\n")

    def summarize_dialogue_with_zero_shot_inference(self):
        for i, index in enumerate(self.test_data_indices):
            dialogue = self.dataset["test"][index]["dialogue"]
            summary = self.dataset["test"][index]["summary"]

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
            print("Example ", i + 1)
            print(self.dash_line)
            print("INPUT PROMPT:\n", prompt, end="\n")
            print(self.dash_line)
            print("BASELINE HUMAN SUMMARY:", summary, end="\n")
            print("MODEL GENERATION - ZERO SHOT:", decoded_dialogue, end="\n")

    def summarize_dialogue_with_one_shot_inference(self):
        for i, index in enumerate(self.test_data_indices):
            dialogue = self.dataset["test"][index]["dialogue"]
            summary = self.dataset["test"][index]["summary"]
            topic = self.dataset["test"][index]["topic"]

            # Prepare one shot prompt
            training_data_index = self.get_random_type_indices("train", topic, 1).pop()
            one_shot_dialogue = self.dataset["train"][training_data_index]["dialogue"]
            one_shot_summary = self.dataset["train"][training_data_index]["summary"]
            one_shot_prompt = f"Dialogue:\n{one_shot_dialogue}\nSummary:\n{one_shot_summary}\n"

            prompt = f"{one_shot_prompt}\nDialogue:\n{dialogue}\nSummary:\n"

            encoded_dialogue = self.tokenizer(prompt, return_tensors="pt")
            decoded_dialogue = self.tokenizer.decode(
                self.model.generate(
                    encoded_dialogue["input_ids"],
                    max_new_tokens=50,
                )[0],
                skip_special_tokens=True
            )
            print(self.dash_line)
            print("Example ", i + 1)
            print(self.dash_line)
            print("INPUT PROMPT:\n", prompt, end="\n")
            print(self.dash_line)
            print("BASELINE HUMAN SUMMARY:", summary, end="\n")
            print("MODEL GENERATION - ONE SHOT:", decoded_dialogue, end="\n")

    # def summarize_dialogue_with_few_shot_inference(self, training_data_indices=[100, 300, 500]):
    #     # Prepare few shot prompt
    #     few_shot_prompt = ""
    #     for i, training_index in enumerate(training_data_indices):
    #         few_shot_dialogue = self.dataset["test"][training_index]["dialogue"]
    #         few_shot_summary = self.dataset["test"][training_index]["summary"]
    #         few_shot_prompt += f"\nDialogue #{i + 1}:\n{few_shot_dialogue}\nSummary #{i + 1}:\n{few_shot_summary}\n"
    #
    #     # Preparing test prompt
    #     final_index = len(training_data_indices) + 1
    #     for i, index in enumerate(self.test_data_indices):
    #         dialogue = self.dataset["test"][index]["dialogue"]
    #         summary = self.dataset["test"][index]["summary"]
    #
    #         prompt = f"{few_shot_prompt}\nDialogue #{final_index}:\n{dialogue}\nSummary #{final_index}:\n"
    #
    #         encoded_dialogue = self.tokenizer(prompt, return_tensors="pt")
    #         decoded_dialogue = self.tokenizer.decode(
    #             self.model.generate(
    #                 encoded_dialogue["input_ids"],
    #                 max_new_tokens=50,
    #             )[0],
    #             skip_special_tokens=True
    #         )
    #         print(self.dash_line)
    #         print("Example ", i + 1)
    #         print(self.dash_line)
    #         print("INPUT PROMPT:\n", prompt, end="\n")
    #         print(self.dash_line)
    #         print("BASELINE HUMAN SUMMARY:", summary, end="\n")
    #         print("MODEL GENERATION - FEW SHOT:", decoded_dialogue, end="\n")


if __name__ == "__main__":
    sd = SummarizeDialogue()
    # sd.view_dataset("test")
    # sd.explore_dataset_by_type("transportation", "test")
    # sd.explore_dataset_by_type("job application", "train")
    # sd.summarize_dialogue_without_prompt_engineering()
    # sd.summarize_dialogue_with_zero_shot_inference()
    sd.summarize_dialogue_with_one_shot_inference()
    # sd.summarize_dialogue_with_few_shot_inference()

