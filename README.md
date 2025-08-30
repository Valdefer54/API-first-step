# Colombia COVID-19 Data Viewer

This project is a command-line interface (CLI) tool built in Python that allows users to query COVID-19 case data in Colombia, filtered by department. The application fetches up-to-date information from Colombia's Open Data API (a Socrata Open Data API).

## Features

- **Interactive Queries**: Allows the user to input a department name and the number of records to retrieve.
- **Error Handling**: Informs the user if no data is found for a specific department or if an error occurs during the API call.
- **Simple Display**: Shows the fetched data in a clean, readable format directly in the terminal.
- **Modular Structure**: The code is organized into modules for the API client (`api/`) and the user interface (`ui/`), following a separation of concerns approach.

## Installation

Follow these steps to set up the environment and run the project locally.

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Valdefer54/API-first-step/
    cd API-first-step
    ```

2.  **Create and Activate a Virtual Environment**
    It is highly recommended to use a virtual environment to isolate project dependencies.
    ```bash
    # Create the environment
    python3 -m venv venv

    # Activate on Linux/macOS
    source venv/bin/activate

    # Activate on Windows
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    The `requirements.txt` file contains all the necessary libraries.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the dependencies are installed, you can run the application with the following command:

```bash
python3 main.py
```

The application will welcome you and prompt you to enter the name of the department and the number of records you wish to see.

```

## Dependencies

This project uses the following Python libraries:

- `pandas`: For data manipulation and display.
- `sodapy`: As a client to interact with the Socrata Open Data API (SODA).
- `pytest`: For running tests.
