import json
from requests_html import HTMLSession


def parsing(url: str):
    session = HTMLSession()

    url_users = f'{url}users/page'
    users = []


    for i in range(1, 6):
        response = session.get(f'{url_users}{i}')
        response.html.render(timeout=100)
        usernames = response.html.find('.tm-user-snippet__nickname')
        
        for user in usernames:
            username = user.text[1:]
            
            url_posts = f'{url}users/{username}/posts/'
            print(url_posts)
            response = session.get(url_posts)
            response.html.render(timeout=100)
            
            posts_unformated = response.html.find('.tm-articles-list__item')
            posts = []
            
            for post in posts_unformated:
                title = post.find('.tm-article-snippet__title-link', first=True).text
                text = post.find('.article-formatted-body, .article-formatted-body, .article-formatted-body_version-2', first=True).text
                image = post.find('.tm-article-snippet__lead-image', first=True)
                
                if image is not None:
                    image = image.attrs['src']

                
                posts.append(
                    {
                        "title": title,
                        "text": text,
                        "image": image
                    }
                )
            

            users.append(
                {
                    "username": username,
                    "posts": posts
                }
            )


    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, indent=2, ensure_ascii=False)
