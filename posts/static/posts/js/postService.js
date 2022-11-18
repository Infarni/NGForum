class PostServive {

    constructor( posts = []){ 
       this.posts = posts
    }

    filterBy (search  = ''){
      if (!search.trim()) return this.posts
      
      return this.posts
      .filter(post => post.text.toLowerCase()
      .includes(search.trim().toLocaleLowerCase()) || post.title.toLowerCase()
      .includes(search.trim().toLocaleLowerCase())
        
    )}

    
    }

  