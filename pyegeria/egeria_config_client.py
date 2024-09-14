"""
SPDX-License-Identifier: Apache-2.0
Copyright Contributors to the ODPi Egeria project.

Client to configure the Egeria platform and servers

"""

from pyegeria import (
    FullServerConfig,
)


class EgeriaConfig(FullServerConfig):
    """
    Client for configuring the Egeria Platform and Servers

    Attributes:

        server_name: str
                Name of the server to use.
        platform_url : str
            URL of the server platform to connect to
        user_id : str
            The identity of the user calling the method - this sets a default optionally used by the methods
            when the user doesn't pass the user_id on a method call.
        user_pwd: str
            The password associated with the user_id. Defaults to None

    Methods:
        Inherits methods from FullServerConfig
    """

    def __init__(
        self, server_name: str, platform_url: str, user_id: str, user_pwd: str = None
    ):
        FullServerConfig.__init__(self, server_name, platform_url, user_id, user_pwd)