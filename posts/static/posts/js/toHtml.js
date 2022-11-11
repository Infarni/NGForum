function ellipsis (string = ''){
    if (string.length > 300){
       return string.substring(0, 300) + '...'
    }
    return string
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
        <div> текст : ${ellipsis(post.text)} </div>
        </li>
        `
    }

    paintPosts (posts = []) {
        return posts.map(this.paintPost).join('')
    }
}
