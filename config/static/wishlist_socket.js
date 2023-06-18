const wishlist_name = $('#user-pk').val()

// создаем вебсокет для бронирования и разбронирования
const wishlist_socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/wishlist/'
    + wishlist_name
    + '/'
)

wishlist_socket.onmessage = socket_onmessage
wishlist_socket.onclose = socket_onclose

function socket_onmessage (e) {
    const data = JSON.parse(e.data)
    console.log(data)

    const wish_id = data.wish_id
    const is_busy = data.is_busy
    
    console.log('fdg')
    if (is_busy) {
        $(`#wish-m-${wish_id} .main-wish`).addClass('wish-busy')
        $(`#wish-${wish_id} .busy-text`).fadeIn(0)
        $(`#wish-btn-${wish_id}`).text('Отменить').addClass('wish-btn-busy')
    } else {
        $(`#wish-m-${wish_id} .main-wish`).removeClass('wish-busy')
        $(`#wish-${wish_id} .busy-text`).fadeOut(0)
        $(`#wish-btn-${wish_id}`).text('Забронировать').removeClass('wish-btn-busy')
    }
    $(`#wish-s-${wish_id}`).fadeOut(0)
    wish_clicked.splice(wish_clicked.indexOf(wish_id), 1)
}

function socket_onclose (e) {
    console.log('Соединение закрыто.')
}

$('#wishlist').on('click', '.btn', function () {
    const wish_id = $(this).attr('id').slice(9)
    let code = ''
    if ($(this).hasClass('wish-btn-busy')) {
        code = 'unbook'
    } else {
        code = 'book'
    }
    wishlist_socket.send(JSON.stringify({
        'wish_id': wish_id,
        'code': code,
    }))
})


