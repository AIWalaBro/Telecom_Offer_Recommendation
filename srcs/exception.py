import sys
from srcs.logger import logging

def error_message_detail(error, error_detail:sys):
     _,_,exc_tb = error_detail.exc_info()
     filename = exc_tb.tb_frame.f_code.co_filename
     error_message = "Error Ocurred in python script filename [{0}] line_numeber[{1} error_message[{2}]".format(
         filename,exc_tb.tb_lineno,str(error)
     )
     return error_message
     
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail= error_detail)
        
    def __str__(self):
        return self.error_message
    

    

        