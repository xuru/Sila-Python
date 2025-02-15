import json
import logging
import time
import uuid
from typing import Optional

import requests

from .businessInformation import BusinessInformation
from .businessOperations import BusinessOperations
from .documents import Documents
from .transactions import Transaction
from .users import User
from .wallet import Wallet
from .endpoints import endPoints
from .ethwallet import EthWallet
from .message import cull_null_values, create_body, lower_keys, getMessage
from .schema import Schema

logger = logging.getLogger(__name__)


class App:
    def __init__(
            self,
            tier,
            app_private_key,
            app_handle,
            wallet_class=EthWallet,
    ):
        """Initalize the application
            This lets users initialize the application by providing the tier, application privatekey and application handle
        Args:
            tier  : SANDBOX,PROD etc
            app_private_key : ethereum privat key for the application
            app_handle  : application sila handle (app.silamoney.eth)
        """
        self.wallet_class = wallet_class
        self.session = requests.Session()
        self.tier = tier.lower()
        self.app_private_key = app_private_key
        self.app_handle = app_handle
        self.updateSchema()

        self.business_information = BusinessInformation(self)
        self.business_operations = BusinessOperations(self)
        self.documents = Documents(self)
        self.transactions = Transaction(self)
        self.users = User(self)
        self.wallet = Wallet(self)

    def updateSchema(self):
        """updates schema.py on initialization of app
            This lets users initialize the schema into schema.py for ease of use
        Args:
            None
        """
        endpoint = endPoints["schemaUrl"]
        message = ["header", "entity", "identity", "crypto", "linkAccount"]
        for i in message:
            response = self.get(endpoint % i)
            sch = {response["message"]: response}
            Schema.append(sch)

    def getUrl(self):
        """construct the url endpoint to make api calls
        Args:
            app: the initialized applications
        """
        url = endPoints["apiUrl"]
        if self.tier == "prod":
            apiurl = url % "api"
        else:
            apiurl = url % self.tier
        return apiurl

    def post(self, path, payload, header):
        """makes a post request to the sila_apis
        Args:
            path : path to the endpoint being called
            payload : json msg to be posted
            header  : contains the usersignature and authsignature
        """
        url = self.getUrl()
        endpoint = url + path
        data1 = json.dumps(payload)
        response = self.session.post(endpoint, data=data1, headers=header)

        output = response.json()

        try:
            output["status_code"] = response.status_code
        except:
            pass

        return output

    def postFile(self, path, payload, header, fileContents):
        url = self.getUrl()
        endpoint = url + path
        message = json.dumps(payload)
        files = {"file": fileContents}
        response = requests.post(
            endpoint, data={"data": message}, headers=header, files=files
        )

        output = response.json()

        return output

    def postFileResponse(
            self, path: str, payload: dict, header: dict
    ) -> requests.Response:
        url = self.getUrl()
        endpoint = url + path
        data = json.dumps(payload)
        response = self.session.post(endpoint, data=data, headers=header)

        if response.status_code == 200:
            return response
        else:
            return response.json()

    def postPlaid(self, url, payload):
        """makes a post request to the sila_apis
        Args:
            path : path to the endpoint being called
            payload : json msg to be posted
            header  : contains the usersignature and authsignature
        """
        content = json.dumps(payload)
        response = self.session.post(
            url, data=content, headers={"Content-Type": "application/json"}
        )
        output = response.json()
        return output

    def get(self, path):
        """make a get request using this function
        Args:
            path : path to the endpoint
        """
        endpoint = path
        response = self.session.get(endpoint)
        output = response.json()
        return output

    def setHeader(
            self,
            msg,
            key: Optional[str] = None,
            business_key: Optional[str] = None,
            content_type: Optional[str] = None,
    ):
        """set the application header with usersignature and authsignature
        Args:
            key : ethereum private key for the user
            msg : message being sent should be signed by user
        """
        appsignature = self.wallet_class.signMessage(msg, self.app_private_key)
        header = {"authsignature": appsignature, "User-Agent": "SilaSDK-python/0.2.24"}
        if content_type is not None and content_type == "multipart/form-data":
            pass
        else:
            header[
                "Content-Type"
            ] = "application/json" if content_type is None else content_type
        if key is not None and len(key.strip()) > 0:
            header["usersignature"] = self.wallet_class.signMessage(msg, key.lower())
        if business_key is not None and len(business_key.strip()) > 0:
            header["businesssignature"] = self.wallet_class.signMessage(
                msg, business_key.lower()
            )

        return header

    def createMessage(self, payload, msg_type):
        """creates the message to be sent based on payload from customer
        Args:
            payload:customer message
        """
        payload.update(
            {
                "app_handle": str(self.app_handle),
                "crypto_code": "ETH",
                "relationship": "user",
            }
        )

        if payload.get("reference") is None:
            payload.update({"reference": str(uuid.uuid4())})

        inpt = getMessage(msg_type)
        data = lower_keys(payload)

        inpt = create_body(inpt, data)

        try:
            inpt["header"]["created"] = int(time.time())
        except:
            pass

        inpt = cull_null_values(inpt, payload)
        logger.debug(inpt)

        return inpt

    def postRequest(
            self,
            path: str,
            msg_type: str,
            payload: dict,
            key: Optional[str] = None,
            business_key: Optional[str] = None,
            content_type=None,
            file_contents=None,
    ):
        """post the message and return response
        Args:
            payload:customer message
            path : endpoint
            key :user_private_key
        """
        data = self.createMessage(payload, msg_type)
        logger.debug(data)
        header = self.setHeader(data, key, business_key, content_type)
        response = (
            self.post(path, data, header)
            if file_contents is None
            else self.postFile(path, data, header, file_contents)
        )
        return response

    def postGetFile(
            self, path: str, msg_type: str, payload: dict, key: str
    ) -> requests.Response:
        data = self.createMessage(payload, msg_type)
        header = self.setHeader(data, key)
        response = self.postFileResponse(path, data, header)
        return response
