
import google.generativeai as genai
import json
import time

api_key = "AIzaSyB-qE6V29e4fqngFM49AjJzcz3-mypjzzA"
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')
responses_list = []

def process_prompt(prompt):
    source = "Gemini"
    start_time = time.time()
    response_text = model.generate_content(prompt).text
    end_time = time.time()

    response_record = {
        "Prompt": prompt,
        "Message": response_text.strip(),
        "TimeSent": int(start_time),
        "TimeRecvd": int(end_time),
        "Source": source
    }

    responses_list.append(response_record)

def process_input_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            prompt = line.strip()
            if not prompt:
                continue
            process_prompt(prompt)

def save_responses_to_json(output_file):
    with open(output_file, "w") as outfile:
        json.dump(responses_list, outfile, indent=4)

input_file_path = "input.txt"
output_file_path = "output.json"

process_input_file(input_file_path)
save_responses_to_json(output_file_path)
