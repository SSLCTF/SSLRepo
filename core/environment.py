import os
from dotenv import load_dotenv


def load():
    workdir = os.path.join(os.getcwd(), ".env")

    load_dotenv(dotenv_path=workdir)