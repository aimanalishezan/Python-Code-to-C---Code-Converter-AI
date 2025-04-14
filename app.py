import os 
import io
import sys
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai
from IPython.display import Markdown,display,update_display
import gradio as gr
import subprocess