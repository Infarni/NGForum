
let postService
const toHtml = new ToHTML() 
let currentPage = 1
let rows = 4

const postContainer = document.querySelector('.posts')
const filterBy = document.querySelector('.filter')
const buttonClear = document.querySelector('#clear')
const buttonLoad = document.querySelector('#load')
const testButton = document.querySelectorAll('.posts')

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
    
}

function displayPaginationBtn(page) {
   
    const liEl = document.createElement("li");
    liEl.classList.add('pagination__item')
    liEl.innerText = page

    if (currentPage == page) liEl.classList.add('pagination__item--active');

    liEl.addEventListener('click', () => {
      currentPage = page
      renderPosts(postService.posts, rows, currentPage)

      let currentItemLi = document.querySelector('li.pagination__item--active');
      currentItemLi.classList.remove('pagination__item--active');

      liEl.classList.add('pagination__item--active');
    })
    return liEl;

    
  }

async function startHomePage (){

    const respone = await fetch (`http://127.0.0.1:8000/api/posts/`)
    const data = await respone.json()

    
    postService = new PostServive(data)
    
    
   renderPosts(postService.posts, rows, currentPage)
    
    toHtml.displayPagination(postService.posts, rows)
}

startHomePage ()

