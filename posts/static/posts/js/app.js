
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
        <br>
        <br>
        <img src="${post.author_avatar}" style="height: 50px; width: 50px">
        username : <span>${post.author_username}</span>
        <div><small> id :${post.id}</small>
        назва : ${post.title}</div>
        <div> текст : ${post.text} </div>
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

    start += 3
    const respone = await fetch (`http://127.0.0.1:8000/api/posts&filter=0-${start + 3}`)
    const data = await respone.json()

    postService = new PostServive(data)
    renderPosts(postService.posts)
}

var start = -3

//startHomePage ()

