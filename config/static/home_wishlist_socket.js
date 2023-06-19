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
    if (code === 'book_unbook') {
        // бронирование разбронивание желания
        const wish_id = data.wish_id
        const is_busy = data.is_busy
        
        if (is_busy) {
            $(`#wish-m-${wish_id} .main-wish`).addClass('wish-busy')
            $(`#wish-${wish_id} .busy-text`).fadeIn(0)
        } else {
            $(`#wish-m-${wish_id} .main-wish`).removeClass('wish-busy')
            $(`#wish-${wish_id} .busy-text`).fadeOut(0)
        }
        $(`#wish-s-${wish_id}`).fadeOut(0)
        wish_clicked.splice(wish_clicked.indexOf(wish_id), 1)
    } else if (code === 'wishlist') {
        // получение списка желаний
        wishes = data.wishes
        draw_wishes()
    } else if (code === 'add_wish') {
        // добавление нового желания
        const wish = data.wish
        draw_one_wish(wish, end=false)
    } else if (code === 'delete_wish') {
        // удаление желания
        const wish_id = data.wish_id
        delete_wish(wish_id)
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
    get_wishlist()
}

function get_wishlist () {
    wishlist_socket.send(JSON.stringify({
        'user_id': user_id,
        'code': 'all_wishes',
    }))
}

// нажатие на кнопку управления желанием
$('#wishlist').on('click', '.btn', function () {
    let wish_id = $(this).attr('id').slice(9)
    wishlist_socket.send(JSON.stringify({
        'wish_id': wish_id,
        'code': 'delete_wish',
    }))
})