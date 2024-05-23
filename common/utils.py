import os
import uuid
from datetime import datetime

from django.conf import settings


def save_file_to_folder(picture_file, folder_name):
    storage_type = settings.STORAGE_TYPE

    if storage_type == 'local':
        # Define the folder path where you want to save the pictures
        folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Generate a unique file name for the picture
        file_name = picture_file.name
        extension = file_name.split('.')[-1]

        # replace the file name with a unique name
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        final_file_name = f"{file_name.split('.')[0]}_{uuid.uuid4()}_{timestamp}.{extension}"

        # Limit the file name to 100 characters
        if len(final_file_name) > 100:
            final_file_name = final_file_name[-100:]

        # Join the folder path and the file name
        file_path = os.path.join(folder_path, final_file_name)

        # Open the file in write binary mode and write the picture data
        with open(file_path, 'wb') as destination:
            for chunk in picture_file.chunks():
                destination.write(chunk)

        server_url = settings.SERVER_URL
        file_url = f"{server_url}{file_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL).replace('//', '/')}"

        # Return the file path
        return file_url
    elif storage_type == 's3':
        # Save the picture to s3
        pass
