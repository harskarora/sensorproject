import sys # The sys module, which provides functions and information about the runtime environment, including error traceback.



class CustomException(Exception):

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):

        return self.error_message
    

def error_message_detail(error,error_detail:sys):

    _,_,exc_tb=error_detail.exc_info()

    error_message = f"Error ocurred for python file :  {exc_tb.tb_frame.f_code.co_filename} at line number : {exc_tb.tb_lineno} and error message is : {error}"

    return error_message

"""
try:

  print(1/0)

except Exception as e:

   print(CustomException(str(e),sys))
   
"""