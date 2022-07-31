from http import client
import streamlit as st
import boto3

st.title('Face Recognition using AWS')
img_file=st.file_uploader('Upload Face Image',type=['png','jpg','jpeg'])

if img_file is not None:
    file_details={}
    file_details['name']=img_file.name
    file_details['type']=img_file.type
    file_details['size']=img_file.size
    st.write(file_details)

    with open('input.jpg','wb') as f:
        f.write(img_file.getbuffer())
    Client=boto3.client('rekognition')
    imageSource=open('input.jpg','rb')
    imageTarget=open('nivi.jpg','rb')
    response=Client.compare_faces(
        SimilarityThreshold=70,
        SourceImage={'Bytes':imageSource.read()},
        TargetImage={'Bytes':imageTarget.read()}
    )
    #st.write(response)
    if (len(response['FaceMatches'])>0):
        st.success('Face Matched')
    else:
        st.error('Face Not Matched')