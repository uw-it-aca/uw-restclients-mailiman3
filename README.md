# REST client for the Mailman3 Core REST API
# uw-restclients-mailiman3
Library for interacting with Mailman3 REST API


To use this client, you'll need these settings in your application or script:

    # Specifies whether requests should use live or mocked resources,
    # acceptable values are 'Live' or 'Mock' (default)
    RESTCLIENTS_MAILMAN3_DAO_CLASS='Live'

    # Mailman3 Core API Credentials
    RESTCLIENTS_MAILMAN3_REST_USER
    RESTCLIENTS_MAILMAN3_REST_PASSWORD

    # Mailman3 Core server hostname
    RESTCLIENTS_MAILMAN3_HOST='https://lists.uw.edu'

    # Mailman3 list mail domain name
    RESTCLIENTS_MAILMAN3_MAIL_DOMAIN='lists.uw.edu'

Optional settings:
    # Mailman3 Base Version
    RESTCLIENTS_MAILMAN3_BASE_VERSION='3.0'

    # Customizable parameters for urllib3
    RESTCLIENTS_MAILMAN3_TIMEOUT=5
    RESTCLIENTS_MAILMAN3_POOL_SIZE=10
