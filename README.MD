HI!

API for testing
# Create New User
http://127.0.0.1:8000/auth/users/

# Get Token (POST only)
http://127.0.0.1:8000/restaurant/api-token-auth/

# GET, POST
http://127.0.0.1:8000/restaurant/menu-items/        #Menu
http://127.0.0.1:8000/restaurant/booking/tables/    #Reservations

# PUT, DELETE
http://127.0.0.1:8000/restaurant/menu-items/1       #Menu
http://127.0.0.1:8000/restaurant/booking/tables/1   #Reservations


created users:
login: [lemonadmin, lemonstaff]
password: Little1234

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reservations',
        'HOST' : 'localhost',
        'PORT' : '3306',
        'USER' : 'root',
        'PASSWORD' : '',
    }
}

Have fun!