
from setuptools import setup, find_packages

setup(
    name='babyagi',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['argparse==1.4.0', 'openai==0.27.4', 'chromadb==0.3.21', 'pre-commit>=3.2.0', 'python-dotenv==1.0.0', 'tiktoken==0.3.3', 'llama-cpp-python>=0.1.42']
)
