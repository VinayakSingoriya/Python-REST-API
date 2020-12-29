# If the get data(video_id) is not in our data, then we can abort the request with a message.

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument(
    "views", type=int, help="views of the video required", required=True)
video_put_args.add_argument(
    "likes", type=int, help="likes of the video is required", required=True)

videos = {}


def abort_if_videoID_doesnot_exist(video_id):
    if video_id not in videos:
        abort(404, message="Couldn't find video...")


class Video(Resource):
    def get(self, video_id):        # Used to get something
        abort_if_videoID_doesnot_exist(video_id)
        return videos[video_id]

    def put(self, video_id):         # Used to create something
        args = video_put_args.parse_args()
        # print(args)
        videos[video_id] = args
        return videos[video_id], 201


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
