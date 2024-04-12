
# **Real Estate API**

## **Overview**
The Real Estate API is a Django REST Framework-based web service designed to provide various functionalities related to real estate listings, property requests, and user interactions.

## **Features**
- **Contact Us:** Users can submit inquiries or messages through the Contact Us endpoint.
- **Request Building:** Users can submit requests for specific buildings or properties they are interested in.
- **Authentication:** Utilizes token-based authentication to ensure secure access to endpoints.
- **View Buildings:** Provides endpoints to view all available buildings, retrieve details of a specific building by ID, and filter buildings based on various criteria.
- **User Management:** The project includes another app for user registration, login, and authentication.

## **Endpoints**
1. **/contact/:** POST endpoint to submit inquiries or messages.
2. **/request-building/:** POST endpoint to submit requests for buildings.
3. **/estates/:** GET endpoint to retrieve a list of all available buildings.
4. **/estates/<pk>/:** GET endpoint to retrieve details of a specific building by ID.

## **Technologies Used**
- **Django REST Framework:** Framework for building Web APIs in Python.

django-filters: Provides filtering capabilities for Django REST Framework.
Token-based Authentication: Utilizes token authentication for secure access.
