from setuptools import find_packages, setup

setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'rohan',
    author_email = '1rn21ai098.rohan@gmail.com',
    install_requires = ['openai', 'langchain','streamlit','python-dotenv','PyPDF2'],
    packages = find_packages()
)
