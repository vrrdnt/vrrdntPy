# import httplib2
# import os
# import sys
#
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaFileUpload
# from google_auth_oauthlib.flow import Flow
# from oauth2client.file import Storage
# from oauth2client.tools import argparser, run_flow
#
# # Create the flow using the client secrets file from the Google API
# # Console.
# flow = Flow.from_client_secrets_file(
#     'path/to/client_secrets.json',
#     scopes=['youtube.upload'])
#
# # This OAuth 2.0 access scope allows an application to upload files to the
# # authenticated user's YouTube channel, but doesn't allow other types of access.
# YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"
#
# # This variable defines a message to display if the CLIENT_SECRETS_FILE is
# # missing.
# MISSING_CLIENT_SECRETS_MESSAGE = """
# WARNING: Please configure OAuth 2.0
#
# To make this sample run you will need to populate the client_secrets.json file
# found at:
#
#    %s
#
# with information from the API Console
# https://console.developers.google.com/
#
# For more information about the client_secrets.json file format, please visit:
# https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
# """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
#                                    CLIENT_SECRETS_FILE))
#
# VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")
#
#
# def get_authenticated_service(args):
#     flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
#                                    scope=YOUTUBE_UPLOAD_SCOPE,
#                                    message=MISSING_CLIENT_SECRETS_MESSAGE)
#
#     storage = Storage("%s-oauth2.json" % sys.argv[0])
#     credentials = storage.get()
#
#     if credentials is None or credentials.invalid:
#         credentials = run_flow(flow, storage, args)
#
#     return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
#                  http=credentials.authorize(httplib2.Http()))
#
#
# def initialize_upload(youtube, options):
#     tags = None
#     if options.keywords:
#         tags = options.keywords.split(",")
#
#     body = dict(
#         snippet=dict(
#             title=options.title,
#             description=options.description,
#             tags=tags,
#             categoryId=options.category
#         ),
#         status=dict(
#             privacyStatus=options.privacyStatus
#         )
#     )
#
#     # Call the API's videos.insert method to create and upload the video.
#     insert_request = youtube.videos().insert(
#         part=",".join(body.keys()),
#         body=body,
#         # The chunksize parameter specifies the size of each chunk of data, in
#         # bytes, that will be uploaded at a time. Set a higher value for
#         # reliable connections as fewer chunks lead to faster uploads. Set a lower
#         # value for better recovery on less reliable connections.
#         #
#         # Setting "chunksize" equal to -1 in the code below means that the entire
#         # file will be uploaded in a single HTTP request. (If the upload fails,
#         # it will still be retried where it left off.) This is usually a best
#         # practice, but if you're using Python older than 2.6 or if you're
#         # running on App Engine, you should set the chunksize to something like
#         # 1024 * 1024 (1 megabyte).
#         media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
#     )
#
#
# if __name__ == '__main__':
#     argparser.add_argument("--file", required=True, help="Video file to upload")
#     argparser.add_argument("--title", help="Video title", default="Test Title")
#     argparser.add_argument("--description", help="Video description",
#                            default="Test Description")
#     argparser.add_argument("--category", default="22",
#                            help="Numeric video category. " +
#                                 "See https://developers.google.com/youtube/v3/docs/videoCategories/list")
#     argparser.add_argument("--keywords", help="Video keywords, comma separated",
#                            default="")
#     argparser.add_argument("--privacyStatus", choices=VALID_PRIVACY_STATUSES,
#                            default=VALID_PRIVACY_STATUSES[0], help="Video privacy status.")
#     args = argparser.parse_args()
#
#     if not os.path.exists(args.file):
#         exit("Please specify a valid file using the --file= parameter.")
#
#     youtube = get_authenticated_service(args)
