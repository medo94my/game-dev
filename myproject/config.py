# Statement for enabling the development environment
DEBUG = False

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
APPLICATION_ROOT="/auth"
# Define the database - we are working with
# SQLite for this example
MONGODB_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS=True
# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "EH5E9jL4M0dDLnLkxKQobQ"

# Secret key for signing cookies
SECRET_KEY = "T4RkCF2If0QFjjS23oCoKw"