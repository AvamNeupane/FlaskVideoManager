# Video API

A Flask REST API that lets you create, read, update, and delete video records. You can add videos, get their info, update view/like counts, and remove videos from the database.

## Video Data
Each video has:
- `id` - unique number
- `name` - video title  
- `views` - view count
- `likes` - like count

## Database
Uses SQLite database (`database.db`) - created automatically.
