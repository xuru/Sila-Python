from .endpoints import endPoints
from .http_client import HttpClient
from .message import Message
import time



class User():


    def __init__(self):
        pass



    def checkHandle(self,user_handle):
         """Check if the user handle is available.
            These endpoint returns the validity of a user handle
        Args:
            payload : Required user_handle to check if its available
        Returns:
            dict: response body (a confirmation message)
        """
       path=endPoints["checkHandle"]
       data=Message.getSchema(path)
       data["header"]["user_handle"]=user_handle
       data["header"]["auth_handle"]=self.app_handle
       reponse=HttpClient.post(path,data,header)
       if response["status"]=="SUCCESS":
           return True




    def register(self,payload,user_private_key):
        
        """Register a new user.
           This user will be kyced and ethereum address will be registered with sila 
        Args:
            payload : info about user like name,ssn, dob,ethereum address, ethereum handle etc
            header: signature in the header using for ethereum key being sent
        Returns:
            dict: response body (a confirmation message)
        """
        header=HttpClient.setHeader(user_private_key)
        path = endPoints["createEntity"]
        

        reponse=HttpClient.post(path,data,header)

        return response
        
       

        
    def checkKyc(payload,header):

        """check if the user has been kyced.
           The used will be checked if the they have been kyced
        Args:
            payload : includes 
            header: signature in the header using for ethereum key being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["checkKyc"]
            
        response=HttpClient.post(path,payload,header)

        return response

    
    def addCrypto(payload,header):

        """check if the user has been kyced.
           The used will be checked if the they have been kyced
        Args:
            payload : includes the crypto adddress, handle etc that need to be added
            header: signature in the header using for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["addCrypto"]
            
        response=HttpClient.post(path,payload,header)

        return response


    def addIdentity(payload,header):
        
        """change the info about user like change ssn, email ,etc.
           The used will be checked if the they have been kyced
        Args:
            payload : includes information to be edited and usee handle
            header: signature in the header using for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["addIdentity"]
            
        response=HttpClient.post(path,payload,header)

        return response

    
    def  createBond(payload,header):
        
        """bond a user handle to an app
           The user will be checked if the they have been kyced, alonf with app
        Args:
            payload : includes information to be edited and user handle
            header: signature in the header used for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["createBond"]
            
        response=HttpClient.post(path,payload,header)

        return response


    def checkhandle(payload,header):
        
        """check if the user handle is taken
           The user handle will be checked if it has been taken
        Args:
            payload : includes information to be edited and user handle
            header: signature in the header used for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["checkHandle"]
            
        response=HttpClient.post(path,payload,header)

        return response
    

    def verifyAccount(payload,header):
        
        """verify the users account
        Args:
            payload : includes information to be edited and user handle
            header: signature in the header used for ethereum address being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["verifyAccount"]
            
        response=HttpClient.post(path,payload,header)

        return response
    

    def linkAccount(payload,header):
        
        """link bank account of a new user.
           This will link account using plad
        Args:
            payload : info about user like  ethereum handle abd bank account info
            header: signature in the header using for ethereum key being sent
        Returns:
            dict: response body (a confirmation message)
        """
        path= endPoints["linkAccount"]

        response=HttpClient.post(path,payload,header)

        return response
    

    def registerOperator(payload,header):
        
        """register developer as an account oprator for ethereum to make transactions on users behalf 
           This will register the operator
        Args:
            payload : ethereum handles
            header: signature in the header using for ethereum key being sent from developer and user
        Returns:
            dict: response body (a confirmation message)
        """
        path= endPoints["registerOperator"]

        response=HttpClient.post(path,payload,header)

        return response
    
    
    
        

    


    

        
        



        