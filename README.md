
# Django Todo App

![Django Todo App Logo](https://cdni.iconscout.com/illustration/free/thumb/free-task-list-2080780-1753768.png)

A simple yet powerful Todo list application built with Django, designed to help you organize your tasks efficiently.

## Features

- **User Authentication**: Users can sign up, log in, and manage their tasks securely.
- **Create, Read, Update, Delete (CRUD) Operations**: Perform all basic CRUD operations on tasks effortlessly.
- **Priority Levels**: Assign priority levels to tasks to manage them effectively.
- **Filtering and Sorting**: Filter and sort tasks based on priority, date, or completion status.
- **Responsive Design**: Access the app seamlessly from any device - desktop, tablet, or mobile.

## Installation

### Using Docker

1. Clone the repository:

    ```bash
    git clone https://github.com/sinanazem/django-todo-app.git
    ```

2. Navigate into the project directory:

    ```bash
    cd django-todo-app
    ```

3. Build and start the Docker containers:

    ```bash
    docker-compose up --build
    ```

4. Visit `http://127.0.0.1:8000` in your browser to access the application.

### Without Docker

If you prefer not to use Docker, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/sinanazem/django-todo-app.git
    ```

2. Navigate into the project directory:

    ```bash
    cd django-todo-app
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Visit `http://127.0.0.1:8000` in your browser to access the application.

## Usage

1. **Sign Up**: Create a new account or log in if you already have one.
2. **Add Tasks**: Click on the "Add Task" button to create a new task. Provide a title, description, and select the priority level.
3. **Update Tasks**: Click on a task to view its details. You can edit or delete the task from there.
4. **Filter and Sort**: Use the filter and sort options to organize your tasks based on priority, date, or completion status.
5. **Mark as Completed**: Once a task is completed, click on the checkbox to mark it as done.

## Contributing

Contributions are welcome! Here's how you can contribute to this project:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

Please make sure to update tests as appropriate and adhere to the [Python PEP 8](https://www.python.org/dev/peps/pep-0008/) coding style.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Hat tip to anyone whose code was used
- Inspiration
- etc.

## Contact

For any inquiries or feedback, please contact [Sina Nazem](mailto:sinanazemm@gmail.com).

