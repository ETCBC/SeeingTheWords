from imagekitio import ImageKit
import os

from imagekitio.models.ListAndSearchFileRequestOptions import ListAndSearchFileRequestOptions


def setup():
    return ImageKit(
        private_key='????????',
        public_key='public_kRnwmhVYMoavSB9Eqsc0gEc8rKw=',
        url_endpoint='https://ik.imagekit.io/seeingthewords'
    )


def get_image(path):
    return setup().url({
        "path": path,
        "url_endpoint": "https://ik.imagekit.io/seeingthewords/"
    })

def get_file_details(path):
    return setup().list_files(options=ListAndSearchFileRequestOptions(path=path,
                                                                      search_query = 'format ="jpg"'
                                                                      )).response_metadata.raw
def get_target_data(target):
   data = setup().list_files().response_metadata.raw
   temp = []
   for image in data:
       if target in image['filePath'] and image[ 'fileType'] == 'image':
           temp.append(image)
   return temp

