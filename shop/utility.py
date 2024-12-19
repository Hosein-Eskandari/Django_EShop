from datetime import datetime
import os

def upload_file_with_date(base_dir='images', sub_dir='products'):
    def wrapper(instance, filename):
        date = datetime.now().strftime('%Y-%m-%d')
        base_filename, file_extension = os.path.splitext(filename)
        new_filename = f'{base_filename}_{datetime.now().strftime('%H%M%S')}{file_extension}'
        return f'{base_dir}/{sub_dir}/{date}/{new_filename}'

    return wrapper
