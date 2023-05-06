function add_dish() {
    let dishes_block = document.getElementById('dishesblock')
    let dishes_count = dishes_block.querySelectorAll('select').length

    let elem = document.getElementById('selectedDish_1');
    let clone = elem.cloneNode(true);
    clone.setAttribute('id', 'selectedDish_'.concat(dishes_count + 1))
    clone.setAttribute('name', 'selectedDish_'.concat(dishes_count + 1))
    let div_dish = document.createElement('div')
    div_dish.setAttribute('id', 'dish_'.concat(dishes_count + 1))
    div_dish.appendChild(clone)

    let button = document.createElement('button');
    button.setAttribute('type', 'button');
    button.setAttribute('onclick', 'delete_dish(' + (dishes_count + 1) + ');');
    button.innerHTML = "Удалить блюдо";

    div_dish.appendChild(button);
    dishes_block.appendChild(div_dish);
}

function delete_dish(id) {
    let elem = document.getElementById('dish_'.concat(id));
    elem.remove();
}