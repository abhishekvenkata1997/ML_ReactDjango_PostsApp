# React-Django Image Post Application

**Project Overview:**
This project integrates a React frontend with a Django backend, enabling users to create posts with multiple images. The application also supports a search functionality for both text and image queries, with image search powered by the MobileNetV3Small Python model.

## Backend Models

### Post Model
- **Content:** Text content of the post.
- **timePosted:** Timestamp indicating when the post was created.
- **tags:** String field containing image tags (stored as a string due to SQLite limitations).

### Image Model
- **image:** Image file location in the media folder.
- **post:** ForeignKey connecting each image to a post.

## Functionality

### Post Creation
Users can create posts with text content and multiple images. The MobileNetV3Small model analyzes each image to extract relevant tags during post creation.

### Image Search
The application includes a search bar for users to search for both text and images. The MobileNetV3Small model enhances image searches for accurate results.

## Serializers

### Image Serializer
- Handles JSON data with image IDs and paths.

### Post Serializer
- Includes a nested Image Serializer for managing multiple images.
- Extends the create function to facilitate image tagging using the MobileNetV3Small model.

## Setup Instructions

1. **Clone the repository.**
   ```bash
   git clone <repository_url>
    ```
2. **Configure the Django Backend.**
```bash
cd backend
python manage.py migrate
python manage.py runserver
```
3. **Initialise the React frontend.**
```bash
cd frontend
npm install
npm start
```

##   Access the application

Visit http://localhost:3000 in your browser to access the application.

## Usage

### Create a New Post

- Add text content and upload multiple images.

### Automated Image Tagging

- The application utilizes the MobileNetV3Small model to automatically generate tags for each image.

### Search Functionality

- Use the search bar to perform searches based on both text and image tags.

## Exploration and Contribution

Feel free to explore and enhance the application according to your requirements! If you encounter any issues or have suggestions, please visit the [Issues](<repository_url>/issues) section of this repository.

## Example Image

## <img width="400" alt="image" src="https://github.com/abhishekvenkata1997/ML_ReactDjango_PostsApp/assets/31111993/81cb8b81-0a81-4ff2-9d3a-f96ffca43641">
Get all posts from the backend only once and store to in localStorage, take from the backend only when the state of posts changes from the previous.

## <img width="400" alt="image" src="https://github.com/abhishekvenkata1997/ML_ReactDjango_PostsApp/assets/31111993/6eef0a55-6ddf-4fe5-9805-ebdba810f62b">
Content search, searches for posts and returns the ones that have the same content.
## <img width="400" alt="image" src="https://github.com/abhishekvenkata1997/ML_ReactDjango_PostsApp/assets/31111993/fa9b266d-c7e4-4461-a9e7-36ab05e54dfc">
Image search searches for hidden image tags(Explain in new 'Add New Post' step)
## <img width="400" alt="image" src="https://github.com/abhishekvenkata1997/ML_ReactDjango_PostsApp/assets/31111993/969aefc7-52a5-4ad7-be25-3b83b6f92db7">
- On images being added it gives a small preview of the images before they are added to the Post.
- On image submission, we run a model that gets tags for these newly added images and these tags are added to the Post model for the row, when an image search is done the tags are searched and relevant posts are returned.
**Note:** Please replace `<repository_url>` and `<image_url>` with the actual URLs.




