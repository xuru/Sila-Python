from .endpoints import endPoints
from silasdk import message
from .ethwallet import EthWallet
import time



class User():



    def checkHandle(self,payload):
        """Check if the user handle is available.
        These endpoint returns the validity of a user handle
        Args:
        payload : Required user_handle to check if its available
        Returns:
        dict: response body (a confirmation message)
        """
        path=endPoints["checkHandle"]
        response=message.postRequest(self,path,payload)        
        return response


    def register(self,payload):
        """Register a new user.
           This user will be kyced and ethereum address will be registered with sila 
        Args:
            payload : info about user like name,ssn, dob,ethereum address, ethereum handle etc
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["register"]
        response=message.postRequest(self,path,payload)        
        return response


    def requestKyc(self,payload):
        """Request kyc for a user by handle
           This user will be kyced and ethereum address will be registered with sila 
        Args:
            payload : info about user like name,ssn, dob,ethereum address, ethereum handle etc
        Returns:
            dict: response body (a confirmation message)
        """
        user_handle=payload["user_handle"]
        auth_handle=self.app_handle
        data={
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle":user_handle ,
                "auth_handle": auth_handle,
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "message": "header_msg"
        }
        header={'Content-Type': 'application/json', 'authsignature': '5a7e53ce0710ec1e6d5ae9e3010c96f6227760e797a139a6315d9c20cc6bfc3c65ef345a404eee02ee32e6d3b154c238aab6b63792bbeb7ee5858a82c1c0111b1c'}
        path = endPoints["requestKyc"]
        response=self.post(path,data,header)        
        return response
    
    
    def linkAccount(self,payload,user_private_key):
        """link the bank account of user using plad
           This users bank account will be linked  
        Args:
            payload : need user handle and plad token
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["linkAccount"]
        response=message.postRequest(self,path,payload,user_private_key)        
        return response
       

        
    def checkKyc(self,payload):
        """check if the user has been kyced.
            The user will be checked if the they have been kyced
        Args:
            payload : includes 
        Returns:
            dict: response body (a confirmation message)
        """
        user_handle=payload["user_handle"]
        auth_handle=self.app_handle
        data={
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle":user_handle ,
                "auth_handle": auth_handle,
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "message": "header_msg"
        }
        header={'Content-Type': 'application/json', 'authsignature': '5a7e53ce0710ec1e6d5ae9e3010c96f6227760e797a139a6315d9c20cc6bfc3c65ef345a404eee02ee32e6d3b154c238aab6b63792bbeb7ee5858a82c1c0111b1c'}
        path = endPoints["checkKyc"]
        response=self.post(path,data,header)        
        return response

    
    def addCrypto(self,payload,user_private_key):
        """check if the user has been kyced.
            The used will be checked if the they have been kyced
        Args:
            payload : includes the crypto adddress, handle etc that need to be added
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["addCrypto"]
        response=message.postRequest(self,path,payload,user_private_key)        
        return response


    def addIdentity(self,payload,user_private_key):
        """change the info about user like change ssn, email ,etc.
            The used will be checked if the they have been kyced
        Args:
            payload : includes information to be edited and usee handle
            user_private_key: users ethereum private key 
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["addIdentity"]
        response=message.postRequest(self,path,payload,user_private_key)        
        return response
    

   
    def  getAccounts(self,payload,user_private_key):
        """get the accounts of users registered with sila
            The user will be checked if they have been kyced, along with app
        Args:
            user_hanlde: users handle registered with app
            user_private_key: user private key asscoicated with crypto address
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["getAccounts"]
        response=message.postRequest(self,path,payload,user_private_key)        
        return response



    def  getTransactions(self,payload,user_private_key):
        """get the users transactions registered with ur app
           The user will be checked if they have been kyced, along with app
        Args:
            user_hanlde: users handle registered with app
            user_private_key: user private key asscoicated with crypto address
        Returns:
            dict: response body (a confirmation message)
        """
        path=endPoints["getTransactions"]
        response=message.postRequest(self,path,payload,user_private_key)        
        return response
    
    
     
    


    

        
        



        