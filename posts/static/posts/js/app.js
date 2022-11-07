
const postContainer = document.querySelector('.posts')
let postService


class PostServive {

constructor( posts = []){ 
   this.posts = posts

}
}
class ToHTML {

    paintPost (post) {
        return `<li>
        <small> id :${post.id}</small>
        <small> текст : ${post.title}</small> 
        </li>
        `
    }

    paintPosts (posts = []) {
        return posts.map(this.paintPost).join('')
    }
}
const toHtml = new ToHTML()


function renderPosts (posts) {

    postContainer.innerHTML = toHtml.paintPosts(posts)

}


async function startHomePage (){ 
    const respone = await fetch ('http://127.0.0.1:8000/api/posts')
    const data = await respone.json()

    postService = new PostServive(data)
    renderPosts(postService.posts)
}


startHomePage ()

