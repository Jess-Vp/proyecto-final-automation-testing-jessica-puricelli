@api
Feature: Login API Request

    Scenario: Login valido
        Given la API de Reqres esta disponible
        When se realiza un login valido
        Then el status code debe ser 200


    Scenario: Login sin password
        Given la API de Reqres esta disponible
        When se realiza un login sin contraseña
        Then el status code debe ser 400
        And el mensaje de error debe ser 'Missing password'


