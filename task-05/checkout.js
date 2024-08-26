document.addEventListener('DOMContentLoaded', () => {
    const cartItemsContainer = document.getElementById('cart-items');
    const totalPriceElement = document.getElementById('total-price');
    
    // Retrieve cart data from localStorage
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    let totalPrice = 0;

    cart.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.className = 'product';
        itemElement.innerHTML = `
            <h3>${item.title}</h3>
            <p>$${item.price}</p>
        `;
        cartItemsContainer.appendChild(itemElement);
        totalPrice += item.price;
    });

    totalPriceElement.textContent = totalPrice.toFixed(2);
});
