function editPost(id) {
    fetch('/post/edit/'+id)
        .then(res => res.json())
        .then(data => {
            document.getElementById('title').value = data.title;
            document.getElementById('content').value = data.content;
            document.getElementById('post-form').action = "/post/edit/"+id;
        });
}