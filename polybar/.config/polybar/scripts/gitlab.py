#!/usr/bin/python3

import os
import requests


access_token = os.environ.get('GITLAB_PRIVATE_KEY', '')
state = 'opened'
scope = 'assigned-to-me'


mr_issue_params = {
	'scope': scope,
	'state': state,
	'private_token': access_token
}


todo_params = {
	'state': 'pending',
	'private_token': access_token
}


def get_data(endpoint, params):
	return str(
		len(
			requests.get(
				f'https://gitlab.com/api/v4/{endpoint}',
				params = params
			).json()
		)
	)


merge_requests = get_data('merge_requests', mr_issue_params)
issues = get_data('issues', mr_issue_params)
todos = get_data('todos', todo_params)
print(' | '.join([issues, merge_requests, todos]))