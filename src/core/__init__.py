from typing import Optional

from flask import Flask
from pydantic import HttpUrl

from core.schemas.swagger import OpenAPIContact, OpenAPILicense


class FlaskEasySwagger:
    """
    This object initializes the Flask Easy Swagger extension.
    It is designed to create the initial settings for the OpenAPI specification.
    """

    def __init__(
        self,
        # Metadata about the API
        openapi: str,
        title: str,
        version: str,
        summary: Optional[str] = "",
        description: Optional[str] = "",
        terms_of_service: Optional[HttpUrl] = None,
        contact: Optional[OpenAPIContact] = None,
        license: Optional[OpenAPILicense] = "MIT",
        # Other ...
        app=None,
        path: Optional[str] = "/swagger",
    ):
        """
        Initialize the FlaskEasySwagger instance.

        :param openapi: The OpenAPI version (e.g., "3.0.2").
        :param title: The title of the API.
        :param version: The version of the API.
        :param summary: A short summary of the API.
        :param description: A longer description of the API.
        :param terms_of_service: A URL to the terms of service for the API.
        :param contact: An instance of OpenAPIContact representing the API's contact information.
        :param license: An instance of OpenAPILicense or a string representing the license information (default: "MIT").
        :param app: The Flask application instance (optional).
        :param path: The URL path where the Swagger UI will be available (default: "/swagger").
        """
        self.openapi = openapi
        self.title = title
        self.summary = summary
        self.description = description
        self.terms_of_service = terms_of_service
        self.contact = contact
        self.license = license
        self.version = version
        self.path = path

        if app is not None:
            self.init_app(app)

    def __repr__(self) -> str:
        return f"{self.title}<{self.version}>"

    def init_app(self, app: Flask):
        """
        Initialize a Flask application for use with this extension instance.

        :param app: The Flask application to initialize.
        """

        def swagger():
            return "Swagger UI"

        app.add_url_rule(self.path, view_func=swagger)
