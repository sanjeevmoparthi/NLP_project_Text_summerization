from setuptools import setup, find_packages

setup(
    name='text_summarization_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Optionally list main dependencies here, or just leave empty
    ],
)


with open("README.md","r",encoding = "utf-8") as f:
    long_description  = f.read()


__version__ = "0.0.0"

REPO_NAME = "NLP_project_Text_summerization"
AUTHOR_USER_NAME = "sanjeevmoparthi"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "kumarsanjeev7101@gmail.com"