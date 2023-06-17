let user_id = $('#user-pk').val()
let wishlist_id = $('#wishlist-pk').val()

if (wishlist_id === '') {
    $.ajax({
        url: '/api/wishlist/',
        method: 'post',
        headers: {
            'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        data: {
            'user_id': user_id,
        },
        success: function (response) {
            if (response.status === 'ok') {
                wishlist_id = response.wishlist.id
            }
        }
    })
}

$('#add-btn').click(function (event) {
    event.preventDefault()
    let text = $('#text').val()
    let about = $('#about').val()
    let link = $('#link').val()

    if (text === '') {
        $('#error').fadeIn(200)
    } else {
        
        $.ajax({
            url: '/api/wish/',
            method: 'post',
            headers: {
                'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            data: {
                'user_id': user_id,
                'wishlist_id': wishlist_id,
                'text': text,
                'about': about,
                'link': link
            },
            success: function (response) {
                $('form')[0].reset()
            }
        })
    }
})

$('#text').click(function () {
    $('#error').fadeOut(200)
})