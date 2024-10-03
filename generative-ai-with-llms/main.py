import random

from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig


class SummarizeDialogue:
    # transportation -> 40
    # job application -> 220
    # test_data_indices = [40, 220]

    # order food
    test_data_indices = [524, 1065]
    type_indices = {
        "test": {
            "transportation": [
                4,
                481,
                482
            ],
            "job application": [
                219,
                220
            ],
            "order food": [521, 523, 524, 1008, 1011, 1014, 1065, 1365, 1367, 1472],
        },
        "train": {
            "birthday": [5, 44, 498, 701, 2534, 2582, 6097, 6427, 6741, 8014, 9096],
            "dance": [4, 105, 1643, 3133, 3428, 5663, 7455, 8221, 8458, 11273],
            "take a bus": [26, 1365, 1924, 2824, 4430, 7515, 7972, 8774, 10104, 11223, 12362],
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
            ],
            "order food": [30, 83, 84, 122, 297, 530, 609, 1002, 1097, 1279, 1301, 1506, 1522, 1571, 1572, 1670, 1856,
                           2271, 2283, 2764, 3150, 3499, 3620, 3789, 3856, 3997, 4071, 4212, 4213, 4372, 4400, 4413,
                           4591, 4643, 4722, 4736, 5060, 5082, 5147, 5462, 5563, 5746, 6030, 6068, 6227, 6372, 6376,
                           6721, 7266, 7273, 7577, 7586, 7718, 7861, 8246, 8247, 8267, 8395, 8643, 8938, 8957, 9317,
                           9349, 9595, 9878, 9945, 10201, 10206, 11122, 11127, 11617, 11619, 11761, 11762, 11872, 12220,
                           12245, 12333, 12450],
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

    def explore_dataset_by_type(self, dataset_type="train"):
        # Viewing Datasets
        topic_frequency = dict()
        print(self.dash_line)
        print("Explore Dataset Type:", dataset_type)
        index = 0
        for item in self.dataset[dataset_type]:
            if item["topic"] not in topic_frequency:
                topic_frequency[item["topic"]] = []
            topic_frequency[item["topic"]].append(index)

            # print(self.dash_line)
            # print("INDEX:\n", index, end="\n")
            # print(self.dash_line)
            # print("ID:\n", item["id"], end="\n")
            # print(self.dash_line)
            # print("DIALOGUE:\n", item["dialogue"], end="\n")
            # print(self.dash_line)
            # print("SUMMARY:\n", item["summary"], end="\n")
            # print(self.dash_line)
            # print("TOPIC:\n", item["topic"], end="\n")
            # print(self.dash_line, end="\n")
            index += 1
        print("Topic Frequency:\n", topic_frequency)

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
            print("BASELINE HUMAN SUMMARY:\n", summary, end="\n")
            print("MODEL GENERATION - ZERO SHOT:\n", decoded_dialogue, end="\n")

    def summarize_dialogue_with_one_shot_inference(self):
        for i, index in enumerate(self.test_data_indices):
            test_dialogue = self.dataset["test"][index]["dialogue"]
            test_summary = self.dataset["test"][index]["summary"]
            test_topic = self.dataset["test"][index]["topic"]

            # Train Prompt
            training_data_index = self.get_random_type_indices("train", test_topic, 1).pop()
            train_dialogue = self.dataset["train"][training_data_index]["dialogue"]
            train_summary = self.dataset["train"][training_data_index]["summary"]
            train_prompt = f"Dialogue:\n{train_dialogue}\nSummary:\n{train_summary}\n"

            # Test Prompt
            one_shot_prompt = f"{train_prompt}\nDialogue:\n{test_dialogue}\nSummary:\n"

            encoded_prompt = self.tokenizer(one_shot_prompt, return_tensors="pt")
            test_summary_prediction = self.tokenizer.decode(
                self.model.generate(
                    encoded_prompt["input_ids"],
                    max_new_tokens=50,
                )[0],
                skip_special_tokens=True
            )
            print(self.dash_line)
            print("Example ", i + 1)
            print(self.dash_line)
            print("INPUT PROMPT:\n", one_shot_prompt, end="\n")
            print(self.dash_line)
            print("BASELINE HUMAN SUMMARY:\n", test_summary, end="\n")
            print("MODEL GENERATION - ONE SHOT:\n", test_summary_prediction, end="\n")

    def summarize_dialogue_with_few_shot_inference(self):
        for i, index in enumerate(self.test_data_indices):
            test_dialogue = self.dataset["test"][index]["dialogue"]
            test_summary = self.dataset["test"][index]["summary"]
            test_topic = self.dataset["test"][index]["topic"]

            # Train Prompt
            train_prompt = ""
            training_data_indices = self.get_random_type_indices("train", test_topic, 3)
            j = 1
            for training_index in training_data_indices:
                train_dialogue = self.dataset["train"][training_index]["dialogue"]
                train_summary = self.dataset["train"][training_index]["summary"]
                train_prompt += f"\nDialogue #{j}:\n{train_dialogue}\nSummary #{j}:\n{train_summary}\n"
                j += 1

            # Test Prompt
            few_shot_prompt = f"{train_prompt}\nDialogue #{j}:\n{test_dialogue}\nSummary #{j}:\n"

            encoded_prompt = self.tokenizer(few_shot_prompt, return_tensors="pt")
            test_summary_prediction = self.tokenizer.decode(
                self.model.generate(
                    encoded_prompt["input_ids"],
                    max_new_tokens=50,
                )[0],
                skip_special_tokens=True
            )
            print(self.dash_line)
            print("Example ", i + 1, f"\nTopic: {test_topic}")
            print(self.dash_line)
            print("INPUT PROMPT:\n", few_shot_prompt, end="\n")
            print(self.dash_line)
            print("BASELINE HUMAN SUMMARY:\n", test_summary, end="\n")
            print("MODEL GENERATION - FEW SHOT:\n", test_summary_prediction, end="\n")

    def summarize_dialogue_with_few_shot_generative_configuration(self):
        for i, index in enumerate(self.test_data_indices):
            test_dialogue = self.dataset["test"][index]["dialogue"]
            test_summary = self.dataset["test"][index]["summary"]
            test_topic = self.dataset["test"][index]["topic"]

            # Train Prompt
            train_prompt = ""
            training_data_indices = self.get_random_type_indices("train", test_topic, 4)
            j = 1
            for training_index in training_data_indices:
                train_dialogue = self.dataset["train"][training_index]["dialogue"]
                train_summary = self.dataset["train"][training_index]["summary"]
                train_prompt += f"\nDialogue #{j}:\n{train_dialogue}\nSummary #{j}:\n{train_summary}\n"
                j += 1

            # Test Prompt
            few_shot_prompt = f"{train_prompt}\nDialogue #{j}:\n{test_dialogue}\nSummary #{j}:\n"

            generation_config = GenerationConfig(max_new_tokens=60, do_sample=True, temperature=1)

            encoded_prompt = self.tokenizer(few_shot_prompt, return_tensors="pt")
            test_summary_prediction = self.tokenizer.decode(
                self.model.generate(
                    encoded_prompt["input_ids"],
                    generation_config=generation_config,
                )[0],
                skip_special_tokens=True
            )

            print(self.dash_line)
            print("Example ", i + 1, f"\nTopic: {test_topic}")
            print(self.dash_line)
            print("INPUT PROMPT:\n", few_shot_prompt, end="\n")
            print(self.dash_line)
            print("BASELINE HUMAN SUMMARY:\n", test_summary, end="\n")
            print("MODEL GENERATION - FEW SHOT:\n", test_summary_prediction, end="\n")


if __name__ == "__main__":
    sd = SummarizeDialogue()
    # sd.view_dataset("test")
    # sd.explore_dataset_by_type("test")
    # sd.summarize_dialogue_without_prompt_engineering()
    # sd.summarize_dialogue_with_zero_shot_inference()
    # sd.summarize_dialogue_with_one_shot_inference()
    # sd.summarize_dialogue_with_few_shot_inference()
    sd.summarize_dialogue_with_few_shot_generative_configuration()
