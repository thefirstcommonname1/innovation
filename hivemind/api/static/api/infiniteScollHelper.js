//initial count is one
let counter = 1;
//helper will load 15 cards when scrolled to the bottom
const quantity = 15;

document.addEventListener('DOMContentLoaded', load());

window.addEventListener("scroll", () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
});

function load() {
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    //get data for post ranging from start to end
    fetch(`/posts?start=${start}&end=${end}`)
        .then(response => response.json())
        .then(data => {
            data.forEach(addPost);
        });
}

//add new post to the DOM
function addPost(contents) {
    //create li Element
    const post = document.createElement("li");

    //post element gets the returned JSON data
    post.innerHTML = contents;

    //append post to the unorderd list
    document.querySelector("#posts").append(post);
}