import requests
import json
from users.models import CustomUser
from posts.models import *


exec(open('config.py').read())

users = json.loads(requests.get(f'{URL}users').text)
posts = json.loads(requests.get(f'{URL}posts').text)
photos = json.loads(requests.get(f'{URL}photos').text)
comments = json.loads(requests.get(f'{URL}comments').text)


number_users = 1
for user in users:
    print(f'Users download: {number_users}')
    CustomUser.objects.update_or_create(
        id=user['id'],
        username=user['username'],
        email=user['email'],
        password='qwerasdf1234'
    )
    
    number_users += 1

number_posts = 1
for post in posts:
    print(f'Post download: {number_posts}')
    PostModel.objects.update_or_create(
        author=CustomUser.objects.get(id=post['userId']),
        id=post['id'],
        title=post['title'],
        text=post['body'],
        published=True
    )
    
    number_posts += 1


number_comments = 1
for comment in comments:
    username = comment['email'][:comment['email'].find("@")]
    try:
        print(f'Users download: {number_users}')
        print(f'Comments download: {number_comments}')
        CustomUser.objects.update_or_create(
            username=username,
            email=comment['email'],
            password='qwerasdf1234'
        )
        PostCommentModel.objects.update_or_create(
            post=PostModel.objects.get(id=comment['postId']),
            author=CustomUser.objects.get(email=comment['email']),
            id=comment['id'],
            text=comment['body']
        )
        
        number_users += 1
        number_comments += 1
    except:
        pass


number_photos = 1
for photo in photos:
    print(f'Photos download: {number_photos}')
    post_id = PostModel.objects.get(id=photo['albumId']).id
    username = PostModel.objects.get(id=photo['albumId']).author.username
    image = requests.get(photo['url'] + '.jpg').content
    image_id = PostImageModel.objects.last()
    if image_id == None:
        image_id = 1
    else:
        image_id = image_id.id
    filename = f'{PATH}/media/users/{username}/posts/{post_id}/images/{image_id}.png'
    try:
        os.makedirs(f'{PATH}/media/users/{username}/posts/{post_id}/images')
    except FileExistsError:
        pass
    with open(filename, 'wb') as file:
        file.write(image)
    
    PostImageModel.objects.update_or_create(
        post=PostModel.objects.get(id=photo['albumId']),
        image=filename[filename.find("NGForum/media/"):]
    )
    
    number_photos += 1