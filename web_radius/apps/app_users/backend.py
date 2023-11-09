# from radiusauth.backends import RADIUSRealmBackend
#
# RADIUS_SERVERS = {
# 'client1.myproject.com': ('radius.client1.com', 1812, 'S3kr3T'),
# }
#
# class MyRADIUSBackend(RADIUSRealmBackend):
#     def get_server(self, realm):
#         if realm in RADIUS_SERVERS:
#             return RADIUS_SERVERS[realm]
#         return None