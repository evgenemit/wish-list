const wishlist_name = $('#user-pk').val()

// создаем вебсокет для бронирования и разбронирования
let wishlist_socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/wishlist/'
    + wishlist_name
    + '/'
)

wishlist_socket.onopen = socket_open
wishlist_socket.onmessage = socket_onmessage
wishlist_socket.onclose = socket_onclose

function socket_onmessage (e) {
    const data = JSON.parse(e.data)

    const code = data.code
    if (code === 'add_wish') {
        // добавление нового желания
        $('form')[0].reset()
    }
}

function socket_onclose (e) {
    console.log('Соединение закрыто.')
    setTimeout(() => {
        console.log('Подключение.')
        wishlist_socket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/wishlist/'
            + wishlist_name
            + '/'
        )
        wishlist_socket.onopen = socket_open
        wishlist_socket.onmessage = socket_onmessage
        wishlist_socket.onclose = socket_onclose
    }, 5000)
}

function socket_open (e) {
    console.log('Соединение открыто.')
}

$('#add-btn').click(function (event) {
    event.preventDefault()
    let text = $('#text').val()
    let about = $('#about').val()
    let link = $('#link').val()

    if (text === '') {
        $('#error').fadeIn(200)
    } else {
        wishlist_socket.send(JSON.stringify({
            'code': 'add_wish',
            'wishlist_id': wishlist_id,
            'text': text,
            'about': about,
            'link': link
        }))
    }
})