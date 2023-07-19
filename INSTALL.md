# installation

## Requirements

- Python 3.8 or higher
- Flask
- SQLlite3
- Loqate API key

## Installation

1. Clone the repository
2. Create a virtual environment
    This allows to install the dependencies without affecting your system.

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment

    ```bash
    source venv/bin/activate
    ```

4. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

## Running the app

1. Activate the virtual environment

    ```bash
    source venv/bin/activate
    ```

2. Set the environment variables

    ```bash
    export LOQATE_USER=XXXXXX
    export LOQATE_PASSWORD=XXXXX
    ```

3. Run the app

    ```bash
    python3 app.py
    ```

You can access the app at http://localhost:5000