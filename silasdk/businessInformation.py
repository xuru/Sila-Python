from .endpoints import endPoints


class BusinessInformation:
    def __init__(self, app):
        self.app = app

    def getBusinessTypes(self):
        """Gets a list of valid business types that can be registered.
        Args:
        Returns:
            dict: response body (business types)
        """
        path = endPoints["getBusinessTypes"]
        msg_type = "business_types_msg"
        payload = {}
        response = self.app.postRequest(path, msg_type, payload)
        return response

    def getBusinessRoles(self):
        """Retrieves the list of pre-defined business roles.
        Args:
        Returns:
            dict: response body (business roles)
        """
        path = endPoints["getBusinessRoles"]
        msg_type = "business_roles_msg"
        payload = {}
        response = self.app.postRequest(path, msg_type, payload)
        return response

    def getNaicsCategories(self):
        """
        Args:
        Returns:
            dict: response body (business roles)
        """
        path = endPoints["getNaicsCategories"]
        msg_type = "naics_categories_msg"
        payload = {}
        response = self.app.postRequest(path, msg_type, payload)
        return response
