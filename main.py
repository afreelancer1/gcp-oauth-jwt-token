from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession


target_audience = 'your-function-url'
service_account_key = 'your-service-account-json-file'

# use the info to create IDToken object
credentials = service_account.IDTokenCredentials.from_service_account_file(
    service_account_key, target_audience=target_audience)

# make authenticated request session
authed_session = AuthorizedSession(credentials)

# print the token
print(credentials.token)
