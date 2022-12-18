import json
import requests
from users.models import CustomUser
from posts.models import *


exec(open('config.py').read())

with open('data.json', 'r', encoding='utf-8') as file:
    users = json.load(file)

users_number = 1
posts_number = 1

for user in users:
    print(f'\n\nUser downloads: {users_number}\n\n')

    username = user['username']
    
    CustomUser.objects.update_or_create(
        username=username,
        email=f'{username}@example.org',
        password='qwerasdf1234'
    )
    users_number += 1
    
    for post in user['posts']:
        print(f'Post downloads: {posts_number}')

        PostModel.objects.update_or_create(
            author=CustomUser.objects.get(username=user['username']),
            title=post['title'],
            text=post['text'],
            published=True
        )

        if post['image'] is not None:
            post_id = PostModel.objects.last()
            if post_id == None:
                post_id = 1
            else:
                post_id = post_id.id
            username = user['username']
            image_url = post['image']
            if image_url[:6] != 'https:':
                image_url = 'https:' + image_url
            image = requests.get(image_url).content
            image_id = PostImageModel.objects.last()
            if image_id == None:
                image_id = 1
            else:
                image_id = image_id.id
            filename = f'{PATH}{SLASH}media{SLASH}users{SLASH}{username}{SLASH}posts{SLASH}{post_id}{SLASH}images{SLASH}{image_id}.png'
            try:
                os.makedirs(f'{PATH}{SLASH}media{SLASH}users{SLASH}{username}{SLASH}posts{SLASH}{post_id}{SLASH}images')
            except FileExistsError:
                pass
            with open(filename, 'wb') as file:
                file.write(image)
            
            PostImageModel.objects.update_or_create(
                post=PostModel.objects.get(id=post_id),
                image=filename[filename.find("NGForum{SLASH}media{SLASH}"):]
            )
        
        posts_number += 1
