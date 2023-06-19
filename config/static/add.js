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

$('#text').click(function () {
    $('#error').fadeOut(200)
})