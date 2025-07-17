from setuptools import setup, find_packages # Import necessary functions from setuptools

# Open the requirements.txt file and read its content.
# .splitlines() splits the content into a list of strings, one for each line (i.e., each requirement).
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Call the setup function to configure the package.
# This function is the entry point for defining how your project should be built and distributed.
setup(
    name="RAG Medcal Chatbot",  # The name of your package. This is how it will be known.
    version="0.1",              # The current version of your package.
    author="Rohit",         # The name of the package author.
    
    # find_packages() automatically discovers all Python packages (directories containing __init__.py)
    # within your project. This is crucial for including all your application's modules.
    packages=find_packages(),
    
    # Specify the list of external dependencies required by your package.
    # These packages will be automatically installed when your package is installed.
    install_requires=requirements,
)