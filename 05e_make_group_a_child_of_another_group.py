import requests

amp_client_id = 'a1b2c3d4e5f6g7h8i9j0'

amp_api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

# EXAMPLES:
# group_guid = '68665863-74d5-4bc1-ac7f-5477b2b6406e'
# parent_group_guid = 'bfe6abd0-6591-4bf2-a0d3-02efc1cd268e'
group_guid = '<GROUP_GUID>'

parent_group_guid = '<PARENT_GROUP_GUID>'

url = 'https://api.amp.cisco.com/v1/groups/{}/parent'.format(group_guid)

data = {'parent_group_guid':parent_group_guid}

request = requests.patch(url, auth=(amp_client_id, amp_api_key), data=data)

print(request.json())
