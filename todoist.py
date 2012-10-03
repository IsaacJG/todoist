#!/usr/bin/evn python

import requests

BASE_URL = 'https://todoist.com/'
SYNC_URL = 'https://todoist.com/TodoistSync/v2/'

SYNCGET_SUB_URL = 'get'
SYNCANDUPDATE_SUB_URL = 'syncAndGetUpdated'
SYNCSYNC_SUB_URL = 'sync'

LOGIN_SUB_URL = 'API/login'

GETPROJECTS_SUB_URL = 'API/getProjects'
GETPROJECT_SUB_URL = 'API/getProject'
ADDPROJECT_SUB_URL = 'API/addProject'
UPDATEPROJECT_SUB_URL = 'API/updateProject'
DELETEPROJECT_SUB_URL = 'API/deleteProject'

GETLABELS_SUB_URL = 'API/getLabels'
ADDLABEL_SUB_URL = 'API/addLabel'
UPDATELABEL_SUB_URL = 'API/updateLabel'
DELETELABEL_SUB_URL = 'API/deleteLabel'
UPDATELABELCOLOR_SUB_URL = 'API/updateLabelColor'

GETUNCOMPLETEDITEMS_SUB_URL = 'API/getUncompletedItems'
GETALLCOMPLETEDITEMS_SUB_URL = 'API/getAllCompletedItems'
GETCOMPLETEDITEMS_SUB_URL = 'API/getCompletedItems'
GETITEMSBYID_SUB_URL = 'API/getItemsById'
ADDITEM_SUB_URL = 'API/addItem'
UPDATEITEM_SUB_URL = 'API/updateItem'
DELETEITEMS_SUB_URL = 'API/deleteItems'
COMPLETEITEMS_SUB_URL = 'API/completeItems'
UNCOMPLETEITEMS_SUB_URL = 'API/uncompleteItems'

ADDNOTE_SUB_URL = 'API/addNote'
UPDATENOTE_SUB_URL = 'API/updateNot'
DELETENOT_SUB_URL = 'API/deleteNote'
GETNOTES_SUB_URL = 'API/getNotes'

QUERY = 'API/query'

class TodoistSession:
    def __init__(self, email, password):
        self.token = self.__get_api_token(email, password)
    
    def __get_api_token(self, email, password):
        token_request = requests.post('{0}{1}?email={2}&password={3}'.format(BASE_URL, LOGIN_SUB_URL, email, password))
        token = token_request.json['api_token']
        return token


    def sync_get(self):
        request = requests.get('{0}{1}?api_token={2}'.format(SYNC_URL, SYNCGET_SUB_URL, self.token))
        return request.json

    def sync_sync(self, json):
        request = requests.get('{0}{1}?api_token={2}&items_to_sync=[{3}]'.format(SYNC_URL, SYNCSYNC_SUB_URL, self.token, json))
        return request.json

    def sync_and_update(self, items_to_sync=None, projects_timestamps=None):
        if items_to_sync == None and projects_timestamps == None:
            request = requests.get('{0}{1}?api_token={2}'.format(SYNC_URL, SYNCANDUPDATE_SUB_URL, self.token))
        else:
            if not items_to_sync == None and projects_timestamps == None:
                request = requests.get('{0}{1}?api_token={2}&items_to_sync=[{3}]'.format(SYNC_URL, SYNCADUPDATE_SUB_URL, self.token, items_to_sync))
            elif items_to_sync == None and not projects_timestamps == None:
                request = requests.get('{0}{1}?api_token={2}&projects_timestamps=[{3}]'.format(SYNC_URL, SYNCANDUPDATE_SUB_URL, self.token, projects_timestamps))
            else:
                request = requests.get('{0}{1}?api_token={2}&items_to_sync=[{3}]&projects_timestamps=[{4}]'.format(SYNC_URL, SYNCANDUPDATE_SUB_URL, self.token, items_to_sync, projects_timestamps))
        return request.json

                
        
    def get_projects(self):
        request = requests.get('{0}{1}?api_token={2}'.format(BASE_URL, GETPROJECTS_SUB_URL, self.token))
        return request.json

    def get_project(self, project_id):
        request = requests.get('{0}{1}?api_token={2}&project_id={3}'.format(BASE_URL, GETPROJECT_SUB_URL, self.token, project_id))
        return request.json

    def add_project(self, name, color=None):
        if color == None:
            request = requests.get('{0}{1}?api_token={2}&name={3}'.format(BASE_URL, ADDPROJECT_SUB_URL, self.token, name))
        else:
            request = requests.get('{0}{1}?api_token={2}&name={3}&color={4}'.format(BASE_URL, ADDPROJECT_SUB_URL, self.token, name, color))
        return request.json

    def update_project(self, *args, **kwargs):
        req_str = '{0}{1}?api_token={2}&project_id={3}'
        for key in kwargs:
            if key == 'name':
                req_str += '&name={0}'.format(kwargs[key])
            elif key == 'color':
                req_str += '&color={0}'.format(kwargs[key])
            elif key == 'indent':
                req_str += '&indent={0}'.format(kwargs[key])
            elif key == 'order':
                req_str += '&order={0}'.format(kwargs[key])
            elif key == 'collapsed':
                req_str += '&collapsed={0}'.format(kwargs[key])
        request = requests.get(req_str.format(BASE_URL, UPDATEPROJECT_SUB_URL, self.token, args[0]))

        return request.json
    def delete_project(self, project_id):
        request = requests.get('{0}{1}?api_token={2}&project_id={3}'.format(BASE_URL, DELETEPROJECT_SUB_URL, self.token, project_id))
        return request.json




    def get_labels(self, project_id):
        request = requests.get('{0}{1}?api_token={2}&project_id={3}'.format(BASE_URL, GETLABELS_SUB_URL, self.token, project_id))
        return request.json

    def add_label(self, name):
        request = requests.get('{0}{1}?api_token={2}&name={3}'.format(BASE_URL, ADDLABEL_SUB_URL, self.token, name))
        return request.json

    def update_label(self, old_name, new_name):
        request = requests.get('{0}{1}?api_token={2}&old_name={3}&new_name={4}'.format(BASE_URL, UPDATELABEL_SUB_URL, self.token, old_name, new_name))
        return request.json

    def update_label_color(self, name, color):
        request = requests.get('{0}{1}?api_token={2}&name={3}&color={4}'.format(BASE_URL, UPDATELABELCOLOR_SUB_URL, self.token, name, color))
        return request.json

    def delete_label(self, name):
        request = requests.get('{0}{1}?api_token={2}&name={3}'.format(BASE_URL, DELETELABEL_SUB_URL, self.token, name))
        return request.json



    def get_uncompleted_items(self, project_id):
        request = requests.get('{0}{1}?api_token={2}&project_id={3}'.format(BASE_URL, GETUNCOMPLETEDITEMS_SUB_URL, self.token, project_id))
        return request.json

    def get_all_completed_items(self, project_id=None):
        if project_id == None:
            request = requests.get('{0}{1}?api_token={2}'.format(BASE_URL, GETALLCOMPLETEDITEMS_SUB_URL, self.token))
        else:
            request = requests.get('{0}{1}?api_token={2}&project_id={3}'.format(BASE_URL, GETALLCOMPLETEDITEMS_SUB_URL, self.token, project_id))
        return request.json

    def get_completed_items(self, project_id):
        request = requests.get('{0}{1}?api_token={2}&project_id={3}'.format(BASE_URL, GETCOMPLETEDITEMS_SUB_URL, self.token, project_id))
        return request.json

    def get_items_by_id(self, ids):
        request = requests.get('{0}{1}?api_token={2}&ids={3}'.format(BASE_URL, GETITEMSBYID_SUB_URL, self.token, ids))
        return request.json

    def add_item(self, project_id, content):
        request = requests.get('{0}{1}?api_token={2}&project_id={3}&content={4}'.format(BASE_URL, ADDITEM_SUB_URL, self.token, project_id, content))
        return request.json

    def delete_items(self, ids):
        request = requests.get('{0}{1}?api_token={2}&ids={3}'.format(BASE_URL, DELETEITEMS_SUB_URL, self.token, ids))
        return request.json

    def complete_items(self, ids):
        request = requests.get('{0}{1}?api_token={2}&ids={3}'.format(BASE_URL, COMPLETEITEMS_SUB_URL, self.token, ids))
        return request.json

    def uncomplete_items(self, ids):
        request = requests.get('{0}{1}?api_token={2}&ids={3}'.format(BASE_URL, UNCOMPLETEITEMS_SUB_URL, self.token, ids))
        return request.json



    def add_note(self, item_id, content):
        request = requests.get('{0}{1}?api_token={2}&item_id={3}&content={4}'.format(BASE_URL, ADDNOTE_SUB_URL, self.token, item_id, content))
        return request.json

    def update_note(self, note_id, content):
        request = requests.get('{0}{1}?api_token={2}&note_id={3}&content={4}'.format(BASE_URL, UPDATENOTE_SUB_URL, self.token, note_id, content))
        return request.json

    def delete_note(self, item_id, note_id):
        request = requests.get('{0}{1}?api_token={2}&item_id={3}&note_id={4}'.format(BASE_URL, DELETENOTE_SUB_URL, self.token, item_id, note_id))
        return request.json

    def get_notes(self, item_id):
        request = requests.get('{0}{1}?api_token={2}&item_id={3}'.format(BASE_URL, GETNOTES_SUB_URL, self.token, item_id))
        return request.json



    def query(self, queries):
        request = requests.get('{0}{1}?api_token={2}&queries={3}'.format(BASE_URL, QUERY, self.token, queries))
        return request.json



    def custom_request(self, request_str):
        request = requests.get(request_str)
        return request.json
