# Setting Up Environment for LangChain

## Introduction

In this video, we are setting up the environment to start working with LangChain and build generative AI applications. The setup involves creating a virtual environment, installing necessary packages, and getting ready for coding.

## Steps to Set Up the Environment

### 1. Create a Folder for Projects

- Create a project folder where all your code and projects will reside.
- For each end-to-end project, create a separate folder within the main project folder.

### 2. Open VSCode

- Open your project folder in VSCode using two methods:
  - Right-click the folder and select "Open with Code."
  - Copy the path of the folder, open Command Prompt, navigate to the path, and type `code .` to open it in VSCode.

### 3. Create Virtual Environment

- Open the terminal in VSCode by pressing `Ctrl + backtick`.
- In the terminal, create a new virtual environment using Anaconda with the command:
  ```bash
  conda create -p venv python=3.10
  ```

## Confirm the Installation

Confirm the creation by pressing **y** for the default installation.

---

## 4. Install Required Packages

1. **Create a `requirements.txt` file** in the project folder.
2. Add `langchain` to the `requirements.txt` for installation.
3. Activate the environment using:
   ```bash
   conda activate venv
   ```

## 5. Install Additional Packages

- Install `ipykernel` to enable **Jupyter Notebook support** in the virtual environment.
- This is necessary for running Jupyter notebooks, which will be used to learn the concepts initially.

---

## 6. Create a Jupyter Notebook

Once the virtual environment is set up and the necessary packages are installed:

1. Create a new **Jupyter notebook** file for the project.
2. Begin working with **LangChain**.

---

## Summary of Steps

1. **Create** a project folder and open it in **VSCode**.
2. **Set up** a virtual environment using **Anaconda**.
3. **Install** necessary packages (like `langchain` and `ipykernel`).
4. **Create** a `requirements.txt` for package management.
5. **Activate** the virtual environment and install dependencies.
6. **Set up** the Jupyter notebook kernel for development.

---

## Conclusion

The setup process ensures that all dependencies are isolated in the virtual environment, making it easier to manage and maintain the project. The next steps will focus on using **LangChain** for building **generative AI applications**.
