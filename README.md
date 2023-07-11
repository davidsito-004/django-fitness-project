
# Fitness Project: A Django Web App for tracking nutritional goals.

With this app, users can create an account, build custom food lists, and easily track their daily intake of calories and macros.


## Authors

- [David Aragon Rocha](https://www.github.com/davidsito-004)


## Features

- User Registration: Create an account and securely log in.
- Food List Creation: Food List Creation: Build custom food lists with a variety of food options.
- Nutritional Information: Access nutritional details such as calories and macros for each food item.
- Macro Summary: Get a comprehensive overview of your food list macros, goal macros, and remaining macros.



## Installation

1. Clone the repository: `git clone https://github.com/davidsito-004/django-fitness-project.git`.
2. Navigate to the project directory: `cd django-fitness-project`.
3. Create and activate a virtual environment:
   - For Windows: `python -m venv env && .\env\Scripts\activate`.
   - For macOS/Linux: `python3 -m venv env && source env/bin/activate`.
4. Install the project dependencies using `pip install -r requirements.txt`.
5. Create a .env file in the project directory (same level as `manage.py`).
6. Run the following command to generate a random secret key:
   ```
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
7. In the `.env` file, add the following line:
   `SECRET_KEY=your_secret_key`, replacing `your_secret_key` with the secret key generated in step 6.
7. Set up the database and perform migrations using `python manage.py migrate`.
8. Load pre-existing data into the database using fixture files:
   - Run the following command to load the category data:
     ```
     python manage.py loaddata fixtures/category_data.json
     ```
   - Run the following command to load the food data:
     ```
     python manage.py loaddata fixtures/food_data.json
     ```
9. Run the development server using `python manage.py runserver`.
10. Access the web app in your browser: `http://localhost:8000`.

## Documentation

[Fitness Django Project documentation](https://davidsito-004.github.io/django-fitness-project/)

    
## Contributing

Contributions are always welcome!

If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.


## License

[MIT](LICENSE.txt)


## Screenshots

![home](https://github.com/davidsito-004/image-hosting/blob/main/fitness-project-home.jpg?raw=true)

![foods](https://github.com/davidsito-004/image-hosting/blob/main/fitness-project-foods.jpg?raw=true)

![list](https://github.com/davidsito-004/image-hosting/blob/main/fitness-project-list.jpg?raw=true)

![register](https://github.com/davidsito-004/image-hosting/blob/main/fitness-project-register.jpg?raw=true)
