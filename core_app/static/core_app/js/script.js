// Django’s CSRF protection
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


let btns = document.querySelectorAll(".add-button-listener button")

btns.forEach(btn => {
    btn.addEventListener("click", addToList)
})

function addToList(e) {
    let food_id = e.target.value
    // Send the id through the url
    let url = "/add-food/"
    let data = { id: food_id }
    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json", 'X-CSRFToken': csrftoken },
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(data => {
            console.log(data);
            // redirect the user to the list using the list id in the json response
            window.location.href = '/list/' + data.list_id + '/';
        })
        .catch(error => {
            console.log(error)
        })

}