
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

async function clearPosts () {

    postContainer.innerHTML = toHtml.paintPosts()
    end = 0

<<<<<<< HEAD
const respone = await fetch ('http://127.0.0.1:8000/api/')
const data = await respone.json()

postService = new PostServive(data)
renderPosts(postService.posts)
=======
>>>>>>> fcd45e747a79a7d147b7165cbe311dc8f1027b46
}


async function startHomePage (){

    end += 3
    const respone = await fetch (`http://127.0.0.1:8000/api/posts&filter(0-${end})`)
    const data = await respone.json()

    postService = new PostServive(data)
    renderPosts(postService.posts)
}


var end = 0

//startHomePage ()

