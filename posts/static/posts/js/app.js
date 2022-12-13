
let postService
const toHtml = new ToHTML() 
let currentPage = 1
let rows = 5

const postContainer = document.querySelector('.postcontainer')
const filterBy = document.querySelector('.filter')
const buttonClear = document.querySelector('#clear')
const buttonLoad = document.querySelector('#load')

        
buttonClear.addEventListener('click', () => {
    
    renderPosts()
})

buttonLoad.addEventListener('click', () => startHomePage())


filterBy.addEventListener('input', event => {
    const value = event.target.value

    const filter = postService.filterBy(value)
    renderPosts(filter, rows, currentPage)
    
})  


function renderPosts (posts, rows, currentPage) {

    postContainer.innerHTML = toHtml.displayList(posts, rows, currentPage)
    toHtml.showMore()
}

async function startHomePage (){

    const respone = await fetch (`http://127.0.0.1:8000/api/posts/`)
    const data = await respone.json()

    
    postService = new PostServive(data)
    
    
   renderPosts(postService.posts, rows, currentPage)
    
    toHtml.displayPagination(postService.posts, rows)
}

startHomePage ()

