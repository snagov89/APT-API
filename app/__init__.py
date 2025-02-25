import os
import logging
from logging.handlers import TimedRotatingFileHandler
from colorama import Fore, Style, init
from flask import Flask

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Initialize colorama for colored terminal output
init(autoreset=True)

# Get MongoDB connection string for Limiter
mongo_conn_string = os.getenv("mongo_connection_string")
print(mongo_conn_string)

# Flask Rate Limiter
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=mongo_conn_string,
)

def setup_logging():
    """Configures logging for the Flask app."""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)  # Ensure the log directory exists

    log_file = os.path.join(log_dir, "app.log")

    # Set up log formatting
    log_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # Console Handler (for terminal output)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Change to DEBUG for more details
    console_handler.setFormatter(log_formatter)

    # File Handler (rotating log files)
    file_handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=7)
    file_handler.setLevel(logging.INFO)  # Logs INFO and above (INFO, WARNING, ERROR, CRITICAL)
    file_handler.setFormatter(log_formatter)

    # Root Logger Setup
    logging.basicConfig(level=logging.INFO, handlers=[console_handler, file_handler])

    logging.info(Fore.GREEN + "Logging setup complete." + Style.RESET_ALL)

def create_app():
    """Flask App Factory"""
    app = Flask(__name__)

    # Initialize logging
    setup_logging()
    
    limiter.init_app(app)

    # Import blueprints
    from .Routes.api.encode_api import encode_api_blueprint
    from .Routes.api.decode_api import decode_api_blueprint

    # Register blueprints
    app.register_blueprint(encode_api_blueprint)
    app.register_blueprint(decode_api_blueprint)

    logging.info(Fore.CYAN + "Flask app created and blueprints registered." + Style.RESET_ALL)

    return app
