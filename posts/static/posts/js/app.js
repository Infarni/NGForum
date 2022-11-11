
let postService
let end = 0
const toHtml = new ToHTML() 


const postContainer = document.querySelector('.posts')
const filterBy = document.querySelector('.filter')
const buttonClear = document.querySelector('#clear')
const buttonLoad = document.querySelector('#load')


buttonClear.addEventListener('click', () => {
    end = 0
    renderPosts()
})

buttonLoad.addEventListener('click', () => startHomePage())


filterBy.addEventListener('input', event => {
    const value = event.target.value

    const filter = postService.filterBy(value)
    renderPosts(filter)
    
})

function renderPosts (posts) {

    postContainer.innerHTML = toHtml.paintPosts(posts)
}

async function startHomePage (){

    end += 3
    const respone = await fetch (`http://127.0.0.1:8000/api/posts&filter(0-${end})`)
    const data = await respone.json()

    postService = new PostServive(data)
    renderPosts(postService.posts)
}

//startHomePage ()

