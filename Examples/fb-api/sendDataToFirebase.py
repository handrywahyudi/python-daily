import json
import facebook
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import yaml


def main():
    # Read config yaml
    file = open("config.yml", "r")
    cfg = yaml.load(file, Loader=yaml.FullLoader)
    
    # Auth to database using service account
    dbUrl = cfg["firebase"]["db_url"] 
    cred = credentials.Certificate(cfg["firebase"]["credentials"])
    firebase_admin.initialize_app(cred, {'databaseURL':dbUrl})

    # Setup db reference on firebase
    ref = db.reference(cfg["firebase"]["db_ref"])
    info = ref.child(cfg["firebase"]["ref_child"])

    # Setup url graph for facebook 
    token = cfg["facebook"]["token"]
    graph = facebook.GraphAPI(token)
    fields = ['message', 'name', 'picture']
    fields = ','.join(fields)
    data = graph.get_object(cfg["facebook"]["graph_object"], fields = fields)
    feeds = data["data"]

    # Send data to firebase
    send_data = []
    for feed in feeds:
        try:
            send_data.append(feed)
            final_result = json.dumps(send_data, indent=4)
            to_json = json.loads(final_result)
            print(to_json)
            info.set(to_json)
        except:
            print("Error found when sent data.")


if __name__ == "__main__":
    main()
