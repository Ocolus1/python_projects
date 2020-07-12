# # Pulling faces from image
# import face_recognition
# from PIL import Image


# img = face_recognition.load_image_file("")
# loc = face_recognition.face_location(img)

# for face_location in loc:
#     top, right, bottom, left = face_location
#     face_img = img[top:bottom, left:right]

#     PIL_img = Image.fromarray(face_img)
#     PIL_img.show()
#     PIL_img.save(f" {top}.jpg")
    


# # checking if the face is the same

# import face_recognition

# img = face_recognition.load_image_file("")
# encoding_img = face_recognition.face_encodings(img)[0]

# img_nxt = face_recognition.load_image_file("")
# encoding_img_nxt = face_recognition.face_encodings(img_nxt)[0]

# results = face_recognition.compare_faces([encoding_img], encoding_img_nxt)

# if results[0]:
#     print("Face match")
# else:
#     print("Wrong confirmation")


# # face location

# import face_recognition

# img = face_recognition.load_image_file("")  # file location
# loc = d = face_recognition.face_locations(img)  # provides the location in an array up,rght,dwn,lft
# print(loc)
# print(f"There are {len(loc)} people in this image")