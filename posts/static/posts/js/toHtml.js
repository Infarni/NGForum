function ellipsis (string = '', maxlength){
    maxlength = 3400
    if (string.length > maxlength){
       return `${string.substring(0, maxlength)} <button class="test">...ще</button> `
    
       } return string 
    }
class ToHTML {

    paintPost (post) {
        return `<li class="post">
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
        
        const postsEl = document.querySelector('.posts')
        postsEl.innerHTML = ""
        page--
    
        const start = rowPerPage * page
        const end = start + rowPerPage
        const paginatedData = postData.slice(start, end)
    
        return this.paintPosts(paginatedData)
    }

    
    displayPagination(postData, rowPerPage) {
        const paginationEl = document.querySelector('.pagination')

        const pagesCount = Math.ceil(postData.length / rowPerPage)
        const ulEl = document.createElement("ul")
        ulEl.classList.add('pagination__list')
    
        for (let i = 0; i < pagesCount; i++) {
          const liEl = displayPaginationBtn(i + 1)
          ulEl.appendChild(liEl)
        }
        paginationEl.appendChild(ulEl)
      }

      
      
    
}

    

    