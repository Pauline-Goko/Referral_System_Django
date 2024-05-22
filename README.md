# Referral System

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Pauline-Goko/Referral_System_Django.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Referral_System
    ```

3. **Create a virtual environment:**

    It's a good practice to work within a virtual environment to manage dependencies.

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

    On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

5. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Create a superuser (optional):**

    If you need access to the Django admin interface, you can create a superuser.

    ```bash
    python manage.py createsuperuser
    ```

8. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

    The development server should now be running on [http://localhost:8000](http://localhost:8000).

## Usage


To access the endpoints provided by the Referral System, use the following URLs:

 - **Generate Referral Code:**

    [http://localhost:8000/api/referral/generate/](http://localhost:8000/api/referral/generate/)

- **Signup Tracking:**

    [http://localhost:8000/api/referral/signup/](http://localhost:8000/api/referral/signup/)

- **Referral Status Check:**

    [http://localhost:8000/api/referral/status/](http://localhost:8000/api/referral/status/)

You can use tools like cURL or Postman to interact with these endpoints.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/my-feature`)
6. Create a new Pull Request


