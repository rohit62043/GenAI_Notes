import sys

class CustomException(Exception):
    """
    CustomException class to provide more detailed error messages,
    including the file name and line number where the exception occurred.
    It inherits from Python's built-in Exception class.
    """
    def __init__(self, message: str, error_detail: Exception = None):
        """
        Initializes the CustomException.

        Args:
            message (str): A user-friendly message describing the error.
            error_detail (Exception, optional): The original exception object
                                                 that caused this CustomException.
                                                 Defaults to None.
        """
        # Construct the detailed error message using the static method
        self.error_message = self.get_detailed_error_message(message, error_detail)
        
        # Call the constructor of the parent Exception class with the detailed message
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        """
        Static method to extract detailed information about the error,
        including file name and line number from the traceback.

        Args:
            message (str): The primary error message.
            error_detail (Exception): The original exception object.

        Returns:
            str: A formatted string containing the detailed error message.
        """
        # Get information about the current exception being handled
        # exc_info() returns a tuple: (type, value, traceback)
        _, _, exc_tb = sys.exc_info()

        # Extract the file name from the traceback object
        # If exc_tb is None (e.g., if called outside an exception context), default to "Unknown File"
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        
        # Extract the line number from the traceback object
        # If exc_tb is None, default to "Unknown Line"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        
        # Format and return the comprehensive error message
        return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"

    def __str__(self):
        """
        Returns the string representation of the CustomException object.
        This method is called when the exception object is printed or converted to a string.

        Returns:
            str: The detailed error message stored in self.error_message.
        """
        return self.error_message

