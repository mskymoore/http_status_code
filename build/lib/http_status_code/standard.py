from . import StatusCode

# General
successful_request = StatusCode(200, 'Successful request')
bad_request = StatusCode(400, 'Bad request')
unauthorized_request = StatusCode(403, 'The required resource is not found')
resource_not_found = StatusCode(404, 'The required resource is not found')
request_assertion_error = StatusCode(410, 'Request assertion error')

# Authentication
expired_token = StatusCode(431, 'The token is expired')
invalid_token = StatusCode(432, 'The token is invalid')
wrong_token = StatusCode(433, 'Wrong token error (related to refresh and access tokens)')
missing_token = StatusCode(434, 'Missing token')