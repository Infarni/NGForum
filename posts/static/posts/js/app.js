
let postService


const postContainer = document.querySelector('.posts')

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

class PostServive {

    constructor( posts = []){ 
       this.posts = posts
    }
    
        claerHtml (){
          return  this.posts = []
        }
    }

function renderPosts (posts) {

    postContainer.innerHTML = toHtml.paintPosts(posts)

}

 function clearPosts () {
postService.claerHtml()
}


async function startHomePage (){

    end += 5
    const respone = await fetch (`http://127.0.0.1:8000/api/posts&filter(0-${end})`)
    const data = await respone.json()

    postService = new PostServive(data)
    renderPosts(postService.posts)
}


let end = 0

//startHomePage ()

