# import json
#
# sample = """{"type": "Polygon", "coordinates": [[[-72.742942, 41.801399], [-72.742942, 41.926746], [-72.624711, 41.926746], [-72.624711, 41.801399]]]}"""
# j = json.loads(sample)
# # print json.dumps(j.get(['coordinates'],[0]))
#
# print j['coordinates'][0]

# import EmailImage
#
# test = EmailImage.emailimg()
# test.emailwithimg("Fire","Hartford","Rakesh","sanchogeorgek@gmail.com","5","100")

import db_interface

dbtest = db_interface.DBInteract()
dbtest.db_update_post_email()