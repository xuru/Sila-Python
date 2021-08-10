from silasdk import message

from .client import App
from .endpoints import endPoints


class BusinessOperations:
    def __init__(self, app: App):
        self.app = app

    def linkBusinessMember(self, payload, user_private_key, business_private_key):
        """
        Args:
            payload: includes member information.
            user_private_key:
            business_private_key:
        Returns:
            dict: response body (confirmation message)
        """
        path = endPoints["linkBusinessMember"]
        msg_type = "link_business_member_msg"
        response = message.postRequest(
            self.app, path, msg_type, payload, user_private_key, business_private_key
        )
        return response

    def unlinkBusinessMember(self, payload, user_private_key, business_private_key):
        """
        Args:
            payload: includes member information.
            user_private_key:
            business_private_key:
        Returns:
            dict: response body (confirmation message)
        """
        path = endPoints["unlinkBusinessMember"]
        msg_type = "unlink_business_member_msg"
        response = message.postRequest(
            self.app, path, msg_type, payload, user_private_key, business_private_key
        )
        return response

    def certifyBeneficialOwner(self, payload, user_private_key, business_private_key):
        """
        Args:
            payload: includes member information.
            user_private_key:
            business_private_key:
        Returns:
            dict: response body (confirmation message)
        """
        path = endPoints["certifyBeneficialOwner"]
        msg_type = "certify_beneficial_owner_msg"
        response = message.postRequest(
            self.app, path, msg_type, payload, user_private_key, business_private_key
        )
        return response

    def certifyBusiness(self, payload, user_private_key, business_private_key):
        """
        Args:
            payload: includes business information.
            user_private_key:
            business_private_key:
        Returns:
            dict: response body (confirmation message)
        """
        path = endPoints["certifyBusiness"]
        msg_type = "certify_business_msg"
        response = message.postRequest(
            self.app, path, msg_type, payload, user_private_key, business_private_key
        )
        return response
