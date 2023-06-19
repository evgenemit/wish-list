function draw_one_wish (element, end=true) {
    let wish_html = ''
    if (element.is_busy) {
        wish_html = `<div class="wish" id="wish-m-${element.id}">
                <div class="main-wish border rounded wish-busy">
                    <div class="wish-clicked" id="wish-${element.id}">
                    <p class="busy-text">Уже занято!</p>
                    <p>${element.text}</p>`
    } else {
        wish_html = `<div class="wish" id="wish-m-${element.id}">
                <div class="main-wish border rounded">
                    <div class="wish-clicked" id="wish-${element.id}">
                    <p class="busy-text" style="display: none">Уже занято!</p>
                    <p>${element.text}</p>`
    }
    if (element.about)
    wish_html += `<div class="about"><small class="text-secondary">${element.about}</small></div>`
    wish_html += `</div>`
    if (element.link)
    wish_html += `<a href="${element.link}" class="text-secondary">${element.link}</a>`
    wish_html += `<div class="wish-settings" style="display: none" id="wish-s-${element.id}"><div class="pt-3 pb-2 d-flex justify-content-between w-100">
    <button class="btn btn-outline-secondary" id="wish-btn-${element.id}">Удалить</button></div></div></div>`

    if (end) {
        $('#wishes').append(wish_html)
    } else {
        $('#wishes').preend(wish_html)
    }
}
