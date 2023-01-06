import os
import json
import requests
from users.models import CustomUser
from posts.models import *


def filling():
    with open(os.path.normpath('data.json'), 'r', encoding='utf-8') as file:
        users = json.load(file)

    users_number = 1
    posts_number = 1

    for user in users:
        print(f'\n\nUser downloads: {users_number}\n\n')

        username = user['username']
        
        if user['avatar'] != None:
            avatar = requests.get(user['avatar']).content
            path = os.path.normpath(f'media/users/{username}/')
            if not os.path.exists(path):
                os.mkdir(path)
            with open(os.path.join(path, 'avatar.jpg'), 'wb') as file:
                file.write(avatar)
            
            CustomUser.objects.update_or_create(
                username=username,
                email=f'{username}@example.org',
                avatar=f'users/{username}/avatar.jpg',
                password='qwerasdf1234'
            )
        else:
            CustomUser.objects.update_or_create(
                username=username,
                email=f'{username}@example.org',
                password='qwerasdf1234'
            )
        
        users_number += 1
        
        for post in user['posts']:
            print(f'Post downloads: {posts_number}')

            Post.objects.update_or_create(
                author=CustomUser.objects.get(username=user['username']),
                title=post['title'],
                text=post['text'],
            )

            if post['image'] is not None:
                post_id = Post.objects.last()
                if post_id == None:
                    post_id = 1
                else:
                    post_id = post_id.id
                username = user['username']
                image_url = post['image']
                if image_url[:6] != 'https:':
                    image_url = 'https:' + image_url
                image = requests.get(image_url).content
                image_id = PostImage.objects.last()
                if image_id == None:
                    image_id = 1
                else:
                    image_id = image_id.id
                filename = os.path.normpath(f'media/users/{username}/posts/{post_id}/images/{image_id}.png')
                try:
                    os.makedirs(os.path.normpath(f'media/users/{username}/posts/{post_id}/images'))
                except FileExistsError:
                    pass
                with open(filename, 'wb') as file:
                    file.write(image)
                
                PostImage.objects.update_or_create(
                    post=Post.objects.get(id=post_id),
                    image=os.path.normpath(f'users/{username}/posts/{post_id}/images/{image_id}.png')
                )
            
            posts_number += 1
