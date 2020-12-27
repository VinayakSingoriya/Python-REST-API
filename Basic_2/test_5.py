# Delete a video and dont create a video that already exists.

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required = True)
video_put_args.add_argument("views", type=int, help="views of the video required", required = True)
video_put_args.add_argument("likes", type=int, help="likes of the video is required", required = True)

videos = {}

def abort_if_videoID_doesnot_exist(video_id):
    if video_id not in videos:
        abort(404, message = "Couldn't find video...")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that id..")
        
class Video(Resource):
    def get(self, video_id):        # Used to get something
        abort_if_videoID_doesnot_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exists(video_id)         # Used to create something
        args = video_put_args.parse_args()
        # print(args)
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_videoID_doesnot_exist(video_id)
        del videos[video_id]
        return " ",204  

                
        
api.add_resource(Video, "/video/<int:video_id>")


                
        


if __name__ == "__main__":
    app.run(debug = True)
