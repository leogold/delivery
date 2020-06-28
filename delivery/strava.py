#from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = '9fa813663a970e9df157e183f8bd26495b8e3596'

# create an instance of the API class
api_instance = swagger_client.ClubsApi()
id = 789 # Long | The identifier of the club.
page = 1 # Integer | Page number. Defaults to 1. (optional)
perPage = 30 # Integer | Number of items per page. Defaults to 30. (optional) (default to 30)

try: 
    # List Club Activities
    api_response = api_instance.getClubActivitiesById(id, page=page, perPage=perPage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubsApi->getClubActivitiesById: %s\n" % e)