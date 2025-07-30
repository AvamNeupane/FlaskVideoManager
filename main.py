from flask import Flask, request 
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) 
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model): #Mini database of videos 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column (db.String(100), nullable=False) #Field cannot be blank (nullable)
    views = db.Column (db.Integer, nullable=False)
    likes = db.Column (db.Integer, nullable=False)

    def __repr__(self):
        return f"Video (name={self.name}, views={self.views}, likes={self.likes})" 


#Check if incoming data is valid wih correct data types
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)


#Check if incoming data is valid wih correct data types for updating
video_patch_args = reqparse.RequestParser()
video_patch_args.add_argument("name", type=str, help="Name of the video")
video_patch_args.add_argument("views", type=int, help="Views of the video")
video_patch_args.add_argument("likes", type=int, help="Likes of the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class Video(Resource):
    @marshal_with(resource_fields)
    #Get Method
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video not found")
        return result, 200
    

    #Put method
    @marshal_with(resource_fields)
    def put (self, video_id):
        args = video_put_args.parse_args()  #Collects data from test using parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video ID already exists...") #If video ID already exists, abort with error message


        video = VideoModel(id=video_id, name= args["name"], views=args["views"], likes=args["likes"]) #Turns data into object
        db.session.add(video)
        db.session.commit()
        return video, 201 #Returning object in JSON using @marshal_with
    
from flask import Flask, request 
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) 
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model): #Mini database of videos 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column (db.String(100), nullable=False) #Field cannot be blank (nullable)
    views = db.Column (db.Integer, nullable=False)
    likes = db.Column (db.Integer, nullable=False)

    def __repr__(self):
        return f"Video (name={self.name}, views={self.views}, likes={self.likes})" 


#Check if incoming data is valid wih correct data types
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)


#Check if incoming data is valid wih correct data types for updating
video_patch_args = reqparse.RequestParser()
video_patch_args.add_argument("name", type=str, help="Name of the video")
video_patch_args.add_argument("views", type=int, help="Views of the video")
video_patch_args.add_argument("likes", type=int, help="Likes of the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class Video(Resource):
    @marshal_with(resource_fields)
    #Get Method
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video not found")
        return result, 200
    

    #Put method
    @marshal_with(resource_fields)
    def put (self, video_id):
        args = video_put_args.parse_args()  #Collects data from test using parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video ID already exists...") #If video ID already exists, abort with error message


        video = VideoModel(id=video_id, name= args["name"], views=args["views"], likes=args["likes"]) #Turns data into object
        db.session.add(video)
        db.session.commit()
        return video, 201 #Returning object in JSON using @marshal_with


    #Patch or update method
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_patch_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video not found")

        # Update only the fields that were provided
        if args["name"] is not None:
            result.name = args["name"]
        if args["views"] is not None:
            result.views = args["views"]
        if args["likes"] is not None:
            result.likes = args["likes"]

        db.session.commit()
        return result, 200



    
    def delete(self, video_id):
        video = VideoModel.query.filter_by(id=video_id).first()
        if video:
            db.session.delete(video)
            db.session.commit()
            return "video has been deleted", 204
    

    
api.add_resource(Video, "/video/<int:video_id>")




        

    
    def delete(self, video_id):
        video = VideoModel.query.filter_by(id=video_id).first()
        if video:
            db.session.delete(video)
            db.session.commit()
            return "video has been deleted", 204
    

    
api.add_resource(Video, "/video/<int:video_id>")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database
    app.run(debug=True)


