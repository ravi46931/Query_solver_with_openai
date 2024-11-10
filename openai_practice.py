from utils.utils import get_completion

def text_summarization(text):
    prompt = f"""
    You are expert in text summarization of the text. \
    Summarize the text delimited by triple backticks \ 
    into a single sentence.
    ```{text}```
    """
    response = get_completion(prompt)
    return response


def few_shot_prompting(text):
    prompt = f"""
    You are expert in few shot prompting of the text. \
    Execute the text delimited by triple backticks \ 
    At most 200 words.
    ```{text}```
    """
    response = get_completion(prompt)
    return response


def custom_steps(text, task, language, output_type):
    prompt = f"""
    You are expert in the following steps. \
    Perform the following actions: 
    1 - {task} the following text delimited by triple \
    backticks with 1 sentence.
    2 - Translate the summary into {language}.
    3 - List each name in the {language} summary.
    4 - Output a {output_type} object \

    Separate your answers with line breaks.
    
    Use the following format:

    Text Summary: <text to summarize>
    Translation: <summary translation>
    Names: <list of names in summary>
    Output : <{output_type}  with summary and num_names>

    Text:
    ```{text}```
    """
    response = get_completion(prompt)
    return response


def description(text):
    prompt = f"""
    You are expert in writing the description of the text. \
    Your task is to help a to people create a 
    description for a given text based 
    on a technical fact sheet.

    Write a complete description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    Technical specifications: ```{text}```
    """
    response = get_completion(prompt)
    return response


def sentiment(text):
    prompt = f"""
    You are expert in analysing the sentiment of the text. \
    What is the sentiment of the following text review, 
    which is delimited with triple backticks?
    Give your answer as a single word, either "positive" \
    or "negative".
    Review text: '''{text}'''
    """
    response = get_completion(prompt)
    return response
