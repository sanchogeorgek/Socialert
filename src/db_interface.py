#Conduit for PostGres DB Connection


import psycopg2
import psycopg2.extras

class DBInteract:

    def db_persist_tweet(self, identifier, handle, twtext, boundingbox):

        try:
            conn = psycopg2.connect("dbname='Socialert' user='socialertapp' host='localhost' port='3991' password='socialertapp_pwd'")

            wktvalid = "ST_AsText(ST_Centroid(ST_MakeValid(ST_SetSRID(ST_GeomFromGeoJSON('" + boundingbox + "'),4326))))"
            geomobject = "ST_Centroid(ST_MakeValid(ST_SetSRID(ST_GeomFromGeoJSON('" + boundingbox + "'),4326)))"

            querycur = conn.cursor()
            querycur.execute(
                """INSERT INTO public.twitter_data(id, tweet_handle, tweet_txt, geojson_wkt, wkt, geom) VALUES (""" + identifier + """,'""" + handle + """','""" + twtext + """','""" + boundingbox + """',""" + wktvalid + """,""" + geomobject + """)""")

            conn.commit()

            print "Logged!"

        except:

            print "Cannot Connect to Database"

    def db_query_email_notification(self):

        # try:
            conn = psycopg2.connect("dbname='Socialert' user='socialertapp' host='localhost' port='3991' password='socialertapp_pwd'")

            querycur = conn.cursor()
            querycur.execute("""SELECT * FROM public.alertview""")
            resultset = querycur.fetchall()
            print "beginning to return!!"
            return resultset
            # for row in resultset:
            # print "  ", row[0],row[1],row[2]



        # except:

            # print "Cannot Connect to Database"


    def db_update_post_email(self, inputid):
        # try:
        conn = psycopg2.connect("dbname='Socialert' user='socialertapp' host='localhost' port='3991' password='socialertapp_pwd'")
        querycur = conn.cursor()
        querycur.execute("""UPDATE public.insured_property_ext SET last_notification_tm = current_timestamp WHERE ID =""" + str (inputid))
        conn.commit()

