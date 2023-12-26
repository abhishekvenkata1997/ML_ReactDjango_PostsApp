import React, { memo, useState } from 'react';
import './../Post.css'

const Post = memo(({ post }) => {
  console.log(post.content) //to check when posts get reloads ]\
  const [currentImage, setCurrentImage] = useState(0);

  //to help move from one image to another both prev and next are used
  const nextSlide = () => {
    const newIndex = (currentImage + 1) % post.images.length;
    setCurrentImage(newIndex);
  };

  const prevSlide = () => {
    const newIndex = (currentImage - 1 + post.images.length) % post.images.length;
    setCurrentImage(newIndex);
  };

  const selectImage = (index) => {
    setCurrentImage(index);
  };

  return (
    <div className="post">
      <h3>{post.content}</h3>
      <div className="postcard">
        <div className="carousel">  
        <div className="carousel-inner" style={{ transform: `translateX(-${currentImage * 100}%)` }}>
            {post?.images.map((image, index) => (
              <div
                key={image.id}
                className="carousel-image-container"
                onClick={() => selectImage(index)} // Click handler for selecting specific image
              >
                <img
                  src={image.image}
                  alt={`Image_val ${image.id}`}
                  className="carousel-image"
                />
              </div>
            ))}
          </div>
        </div>
        {post?.images.length > 1 && (
          <>
            <div className="prev" onClick={prevSlide}>
              &#10094;
            </div>
            <div className="next" onClick={nextSlide}>
              &#10095;
            </div>
          </>
        )}
      </div>
    </div>
  );
});

export default Post;
