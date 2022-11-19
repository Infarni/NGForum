class ToHTML {

    showMore () { 
        const posts = document.querySelectorAll('.posts')
        const buttons = document.querySelectorAll('.button-more')
        
        posts.forEach(post => {
            post.addEventListener('click',(even) => {
                const postMore = post.classList.contains('more')
                const button = even.target.classList.contains('button-more')
                    if(button){
                        post.classList.add('more')
                        even.target.innerText = 'Сховати '
                    }
                    if(button && postMore){
                        post.classList.remove('more')
                        even.target.innerText = 'Показати ще'
                    }
                })      
        })
    }

    paintPost (post) {

        function ellipsis (string = '', maxlength = 300){
        
            if (string.length > maxlength){
               string =  `${string} <button class="button-more">Показати ще</button> `
           
                } return string 
            }
    

        return `<li class="posts">
        <br>
        <br>
        <img src="${post.author_avatar}" style="height: 50px; width: 50px">
        username : <span>${post.author_username}</span>
        <small> id :${post.id}</small>
        назва : ${post.title}
        текст : ${ellipsis(post.text)}
        </li>
        `
    }

    paintPosts (posts = []) {
        
        return posts.map(this.paintPost).join('')
    }


    displayList (postData, rowPerPage, page) {
        
        const postsEl = document.querySelector('.postcontainer')
        postsEl.innerHTML = ""
        page--
    
        const start = rowPerPage * page
        const end = start + rowPerPage
        const paginatedData = postData.slice(start, end)
    
        return this.paintPosts(paginatedData)
    }


    displayPaginationBtn(page) {
   
        const liEl = document.createElement("li");
        liEl.classList.add('pagination__item')
        liEl.innerText = page
    
        if (currentPage === page) liEl.classList.add('pagination__item--active')
    
        liEl.addEventListener('click', () => {
          currentPage = page
          renderPosts(postService.posts, rows, currentPage)
    
          let currentItemLi = document.querySelector('li.pagination__item--active')
          currentItemLi.classList.remove('pagination__item--active')
    
          liEl.classList.add('pagination__item--active')
        })
       
        return liEl
}

    
    displayPagination(postData, rowPerPage) {
        const paginationEl = document.querySelector('.pagination')

        const pagesCount = Math.ceil(postData.length / rowPerPage)
        const ulEl = document.createElement("ul")
        ulEl.classList.add('pagination__list')
    
        for (let i = 0; i < pagesCount; i++) {
          const liEl = this.displayPaginationBtn(i + 1)
          ulEl.appendChild(liEl)
        }
        paginationEl.appendChild(ulEl)
      }
}


    

    