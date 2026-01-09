# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "inflection",
# ]
# ///

import inflection

test_cases = [
    'getActivities',
    'createActivity',
    'albumId',
    'assetId',
    'userId',
    'ActivityCreateDto',
    'Activities',
    'getPlugin',
    'getPluginTriggers',
    'UserUpdateMeDto',
]

print('Testing inflection.underscore() with typical OpenAPI inputs:')
print('=' * 60)
for name in test_cases:
    result = inflection.underscore(name)
    print(f'{name:30} -> {result}')

print('\n' + '=' * 60)
print('Testing edge cases (if they exist in OpenAPI):')
edge_cases = ['get-Activities', 'create Activity', 'album.Id', 'user_id']
for name in edge_cases:
    result = inflection.underscore(name)
    print(f'{name:30} -> {result}')
