# Project "Neobis_Mobi_Market"
Neobis_Mobi_Market is Django Rest Frame based web application. It allows users to register, to login, to edit profile (including photo), to add products for sale
after confirming phone number by 4-digit code sent to email. It also allows users to add products to Favorite by putting a Like. Users can edit and delete products.

## Installation

1. Make sure you have Python version 3.x and pip installed
2. Clone the repository from GitHub:

```bash
git clone git@github.com:Akhambay/Neobis_Mobi_Market.git
```
Install dependecies: 
```bash
pip install -r requirements.txt
```
Perform database migrations
```bash
python manage.py migrate
```
Start development server:
```bash
python manage.py runserver
```
Now your project is available at http://127.0.0.1:8000/ and at https://pavel-backender.org.kg/

## Usage
The following functions are provided in the project:
1. Signing up
2. Logging In
3. Editing profile
4. Confirming user profile by code
5. Add / edit products
6. Add products to Favorite (Put Like)

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
assyl(dot)akhambay(at)gmail.com
