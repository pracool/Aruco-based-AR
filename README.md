# Aruco-based-AR
simple augmented reality using aruco markers 
1. An aruco marker is a fiducial marker that is placed on the object or scene being imaged. It is a binary square with black background and boundaries and a white generated pattern within it that uniquely identifies it. The black boundary helps making their detection easier. They can be generated in a variety of sizes. The size is chosen based on the object size and the scene, for a successful detection. If very small markers are not being detected, just increasing their size can make their detection easier.
2. There are several functions : 
ar.imread(path_of_img) : return image read from the given path.

ar.vidread(path_of_video) : returns video read from the given path.

ar.ar(im,vid): given image and video, it will generate the final video.
