#import all required library 
import os 
import io
import sys
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai
from IPython.display import Markdown,display,update_display
import gradio as gr
import subprocess

#load the key from env file
load_dotenv()

#inetialize the model
openai=OpenAI
#define the model name as you want which model 
OPENAI_MODEL="gpt-4o-mini"


def write_output(code, file_name):
    "Write the generated code to a file."
    with open (file_name, "w") as f:
        f.write(code)
