In Google Cloud, when you set up authentication with HTTP triggers in Cloud Functions then you must pass an OAuth token in your header to invoke your Function.

If you want to use your service account(having Cloud Functions Invoker role) from your local dev environment or want to use it in other programatic way then you must first obtain a JWT OAuth ID token. A simple Access token won't work. A JSON key for the service account and URl for your Function is needed to generate the token.

This script can be used to get that token for authentication purpose. You need to enter your function's url, the JSON key file path and have the Python dependencies (GCP client library) installed for it to work.
