# Mini Akinator
It is a web game in which certain questions are asked to the user and based on the answer, returns a guess which language user was thinking of.


# How to run?
Run the following command and check http://127.0.0.1:5000/
```sh
python app.py
``` 


# Set up
- Create project directory

- Create virtual environment
    http://docs.python-guide.org/en/latest/dev/virtualenvs/ read the guidelines to set up virtual environment.
    
    ```sh
    cd my_project_folder
    virtualenv venv
    virtualenv -p path-to-python3.5 name_of_env
    source venv/bin/activate
    ```
    
    If virtualwrapper is installed then run the following:
    ```sh
    mkvirtualenv -p path-to-python3.5 -a path-to-directory name_of_env
    workon venv
    ```

- Install required packages
    ```sh
    pip install requirements.txt
    ```




