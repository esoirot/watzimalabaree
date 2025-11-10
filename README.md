This project uses pyenv
python 3.14
pipx
Poetry
FastApi
Uvicorn

Project requirements
1 - Python 3.14 and pip installed
2 - Pipx installed
3 - Poetry installed

1 - python 3.14 installation
Recommend of using pyenv as python version manager
follow the tutorials and installation on the official website : https://github.com/pyenv/pyenv

2 - Pipx installation
python 3 -m pip install -user pipx
python3 -m pipx ensurepath
Restart the terminal

3 - Poetry install
After a freshly restarted terminal
pipx install poetry

Install all the project's packages
poetry install


Run the project
poetry run uvicorn watzimalabaree:app --reload
or
poetry shell
uvicorn watzimalabaree:app --reload