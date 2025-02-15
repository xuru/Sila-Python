from .endpoints import endPoints


class Transaction:
    def __init__(self, app):
        self.app = app

    def issue_sila(self, payload: dict, user_private_key: str) -> dict:
        """issues sila erc20token for dollar amount on ethereum blockchain to kyced ethereum addresses (price one cent per token)
            the handle address signatures need to be verified
        Args:
            payload : includes user handle and amount
            user_private_key: users ethereum private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["issueSila"]
        msg_type = "issue_msg"
        response = self.app.postRequest(path, msg_type, payload, user_private_key)
        return response

    def redeemSila(self, payload, user_private_key):
        """redeems sila erc20token for dollar amount on ethereum blockchain to kyced ethereum addresses (price one cent per token)
            the handle address signatures need to be verified
        Args:
            payload : user handle and amount
            user_private_key: users ethereum private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["redeemSila"]
        msg_type = "redeem_msg"
        response = self.app.postRequest(path, msg_type, payload, user_private_key)
        return response

    def transferSila(self, payload, user_private_key, use_destination_address=False):
        """transfer sila from one ethereum address to another using sila api
            the handle address signatures need to be verified
        Args:
            payload : user handle and amount
            user_private_key: users ethereum private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["transferSila"]
        msg_type = "transfer_msg"
        response = self.app.postRequest(path, msg_type, payload, user_private_key)
        return response

    def plaidSamedayAuth(self, payload, user_private_key):
        """Handle a request for a Plaid public_token in order to complete
            Plaid's Same Day Microdeposit Authentication
        Args:
            payload : user handle and amount
            user_private_key: users ethereum private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["plaidSameDayAuth"]
        msg_type = "account_name_msg"
        response = self.app.postRequest(path, msg_type, payload, user_private_key)
        return response

    def cancelTransaction(self, payload, user_private_key):
        """Cancel a pending transaction under certain circumstances


        Args:
            payload : user handle and transaction id
            user_private_key: users ethereum private key
        Returns:
            dict: response body (a confirmation message)
        """
        path = endPoints["cancelTransaction"]
        msg_type = "cancel_transaction_msg"
        response = self.app.postRequest(path, msg_type, payload, user_private_key)
        return response
