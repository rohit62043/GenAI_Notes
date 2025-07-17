import logging  # Import the logging module for logging functionalities
import os       # Import the os module for interacting with the operating system (e.g., creating directories)
from datetime import datetime # Import datetime to get current date and time for log file naming

# Define the directory where log files will be stored
LOGS_DIR = "logs"

# Create the logs directory if it doesn't already exist.
# exist_ok=True prevents an error if the directory already exists.
os.makedirs(LOGS_DIR, exist_ok=True)

# Construct the log file name. It includes the current date to create a new log file daily.
# Example: "logs/log_2025-07-17.log"
LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure the basic logging settings for the root logger.
logging.basicConfig(
    filename=LOG_FILE,  # Specify the file where log messages will be written
    format='%(asctime)s - %(levelname)s - %(message)s', # Define the format of log messages
                                                         # %(asctime)s: Log record creation time
                                                         # %(levelname)s: Text logging level (e.g., INFO, ERROR)
                                                         # %(message)s: The actual log message
    level=logging.INFO  # Set the minimum logging level to INFO.
                        # Messages with severity INFO, WARNING, ERROR, CRITICAL will be logged.
                        # DEBUG messages will be ignored by this configuration.
)

def get_logger(name):
    """
    Returns a named logger instance. This allows for specific loggers
    for different modules or components of the application.

    Args:
        name (str): The name of the logger (e.g., __name__ for module-specific logging).

    Returns:
        logging.Logger: A configured logger instance.
    """
    logger = logging.getLogger(name)  # Get or create a logger with the given name
    logger.setLevel(logging.INFO)     # Set the logging level for this specific logger to INFO
                                      # This ensures that messages at INFO level and higher are processed by this logger
    return logger