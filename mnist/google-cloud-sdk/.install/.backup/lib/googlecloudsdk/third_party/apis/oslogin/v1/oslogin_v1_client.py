"""Generated client library for oslogin version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.oslogin.v1 import oslogin_v1_messages as messages


class OsloginV1(base_api.BaseApiClient):
  """Generated client library for service oslogin version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://oslogin.googleapis.com/'

  _PACKAGE = u'oslogin'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/compute']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'OsloginV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new oslogin handle."""
    url = url or self.BASE_URL
    super(OsloginV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.users_projects = self.UsersProjectsService(self)
    self.users_sshPublicKeys = self.UsersSshPublicKeysService(self)
    self.users = self.UsersService(self)

  class UsersProjectsService(base_api.BaseApiService):
    """Service class for the users_projects resource."""

    _NAME = u'users_projects'

    def __init__(self, client):
      super(OsloginV1.UsersProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      r"""Deletes a POSIX account.

      Args:
        request: (OsloginUsersProjectsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/users/{usersId}/projects/{projectsId}',
        http_method=u'DELETE',
        method_id=u'oslogin.users.projects.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'OsloginUsersProjectsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

  class UsersSshPublicKeysService(base_api.BaseApiService):
    """Service class for the users_sshPublicKeys resource."""

    _NAME = u'users_sshPublicKeys'

    def __init__(self, client):
      super(OsloginV1.UsersSshPublicKeysService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      r"""Deletes an SSH public key.

      Args:
        request: (OsloginUsersSshPublicKeysDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/users/{usersId}/sshPublicKeys/{sshPublicKeysId}',
        http_method=u'DELETE',
        method_id=u'oslogin.users.sshPublicKeys.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'OsloginUsersSshPublicKeysDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Retrieves an SSH public key.

      Args:
        request: (OsloginUsersSshPublicKeysGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SshPublicKey) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/users/{usersId}/sshPublicKeys/{sshPublicKeysId}',
        http_method=u'GET',
        method_id=u'oslogin.users.sshPublicKeys.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'OsloginUsersSshPublicKeysGetRequest',
        response_type_name=u'SshPublicKey',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates an SSH public key and returns the profile information. This method.
supports patch semantics.

      Args:
        request: (OsloginUsersSshPublicKeysPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SshPublicKey) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/users/{usersId}/sshPublicKeys/{sshPublicKeysId}',
        http_method=u'PATCH',
        method_id=u'oslogin.users.sshPublicKeys.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'sshPublicKey',
        request_type_name=u'OsloginUsersSshPublicKeysPatchRequest',
        response_type_name=u'SshPublicKey',
        supports_download=False,
    )

  class UsersService(base_api.BaseApiService):
    """Service class for the users resource."""

    _NAME = u'users'

    def __init__(self, client):
      super(OsloginV1.UsersService, self).__init__(client)
      self._upload_configs = {
          }

    def GetLoginProfile(self, request, global_params=None):
      r"""Retrieves the profile information used for logging in to a virtual machine.
on Google Compute Engine.

      Args:
        request: (OsloginUsersGetLoginProfileRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LoginProfile) The response message.
      """
      config = self.GetMethodConfig('GetLoginProfile')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetLoginProfile.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/users/{usersId}/loginProfile',
        http_method=u'GET',
        method_id=u'oslogin.users.getLoginProfile',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'projectId', u'systemId'],
        relative_path=u'v1/{+name}/loginProfile',
        request_field='',
        request_type_name=u'OsloginUsersGetLoginProfileRequest',
        response_type_name=u'LoginProfile',
        supports_download=False,
    )

    def ImportSshPublicKey(self, request, global_params=None):
      r"""Adds an SSH public key and returns the profile information. Default POSIX.
account information is set when no username and UID exist as part of the
login profile.

      Args:
        request: (OsloginUsersImportSshPublicKeyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ImportSshPublicKeyResponse) The response message.
      """
      config = self.GetMethodConfig('ImportSshPublicKey')
      return self._RunMethod(
          config, request, global_params=global_params)

    ImportSshPublicKey.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/users/{usersId}:importSshPublicKey',
        http_method=u'POST',
        method_id=u'oslogin.users.importSshPublicKey',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'projectId'],
        relative_path=u'v1/{+parent}:importSshPublicKey',
        request_field=u'sshPublicKey',
        request_type_name=u'OsloginUsersImportSshPublicKeyRequest',
        response_type_name=u'ImportSshPublicKeyResponse',
        supports_download=False,
    )
