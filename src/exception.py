# custom exception
''' 
     Sys library hasall the exception informations
'''
import sys 
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()  # Returns 3 values, and the 3rd one has file name, line number, etc.
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in the Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Inherit from the Exception class
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message

# Test the custom exception
#if __name__ == "__main__":
#    try:
#        a = 1 / 0
#    except Exception as e:
#        logging.info("Divided by Zero Error!!!")
#        raise CustomException(e, sys)

