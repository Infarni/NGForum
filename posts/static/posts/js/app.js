
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
        username : <span>${post.author_username}</span>
        <small> id :${post.id}</small>
        <small> назва : ${post.title}</small>
        <div> текст : ${post.text} </div>
        </li>
        <br>
        <br>
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


//startHomePage ()

