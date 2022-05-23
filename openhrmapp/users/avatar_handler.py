import os
import uuid

from PIL import Image
from flask import url_for, current_app


def add_profile_picture(pic_upload):
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    storage_filename = uuid.uuid4() + '.' + ext_type
    filepath = os.path.join(current_app.root_path, 'static/avatars', storage_filename)
    output_size = (32, 32)
    
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)
    
    return storage_filename
    