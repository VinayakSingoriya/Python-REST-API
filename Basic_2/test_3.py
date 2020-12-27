#Introduction to the put request.

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required = True)
video_put_args.add_argument("views", type=int, help="views of the video required", required = True)
video_put_args.add_argument("likes", type=int, help="likes of the video is required", required = True)

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        # print(args)
        videos[video_id] = args
        return videos[video_id], 201
                
        
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug = True)
