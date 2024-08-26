const terminalOutput = document.querySelector('.terminal-output');
const terminalInput = document.querySelector('input[type="text"]');
const productCatalog = document.querySelector('.product-catalog');

let products = [];
let cart = [];

// Fetch products from API
async function fetchProducts() {
    try {
        const response = await fetch('https://fakestoreapi.com/products');
        products = await response.json();
        displayProductsOnScreen();
    } catch (error) {
        terminalOutput.textContent += `Error fetching products: ${error}\n`;
    }
}

// Display products on the screen
function displayProductsOnScreen() {
    productCatalog.innerHTML = ''; // Clear existing content
    if (products.length === 0) {
        terminalOutput.textContent += 'No products available.\n';
        return;
    }
    products.forEach(product => {
        productCatalog.innerHTML += `
            <div class="product">
                <img src="${product.image}" alt="${product.title}" class="product-image">
                <h3>${product.title}</h3>
                <p>$${product.price}</p>
            </div>
        `;
    });
}

// Handle terminal input
function handleInput(command) {
    const [action, ...args] = command.trim().split(' ');

    switch (action) {
        case 'list':
            listProducts();
            break;
        case 'details':
            showProductDetails(args[0]);
            break;
        case 'add':
            addToCart(args[0]);
            break;
        case 'remove':
            removeFromCart(args[0]);
            break;
        case 'cart':
            viewCart();
            break;
        case 'buy':
            buyItems();
            break;
        case 'clear':
            clearTerminal();
            break;
        case 'search':
            searchProducts(args.join(' '));
            break;
        case 'sort':
            sortProducts(args[0]);
            break;
        default:
            terminalOutput.textContent += `Invalid command: ${command}\n`;
            break;
    }

    terminalInput.value = '';
}

// List all products
function listProducts() {
    terminalOutput.innerHTML = 'Available Products:\n';
    products.forEach(product => {
        terminalOutput.innerHTML += `${product.title} - $${product.price}\n`;
    });
}

// Show details of a specific product
function showProductDetails(productId) {
    const product = products.find(p => p.id === parseInt(productId));
    if (product) {
        terminalOutput.innerHTML = `
            Title: ${product.title}
            Price: $${product.price}
            Description: ${product.description}
            Image: ${product.image}
        `;
    } else {
        terminalOutput.textContent += `Product with ID ${productId} not found.\n`;
    }
}

// Add product to cart
function addToCart(productId) {
    const product = products.find(p => p.id === parseInt(productId));
    if (product) {
        cart.push(product);
        terminalOutput.textContent += `Added ${product.title} to cart.\n`;
    } else {
        terminalOutput.textContent += `Product with ID ${productId} not found.\n`;
    }
}

// Remove product from cart
function removeFromCart(productId) {
    const index = cart.findIndex(p => p.id === parseInt(productId));
    if (index !== -1) {
        const removedProduct = cart.splice(index, 1)[0];
        terminalOutput.textContent += `Removed ${removedProduct.title} from cart.\n`;
    } else {
        terminalOutput.textContent += `Product with ID ${productId} not in cart.\n`;
    }
}

// View current items in cart
function viewCart() {
    if (cart.length === 0) {
        terminalOutput.textContent += 'Cart is empty.\n';
        return;
    }
    terminalOutput.innerHTML = 'Current Cart Items:\n';
    cart.forEach(product => {
        terminalOutput.innerHTML += `${product.title} - $${product.price}\n`;
    });
}

// Proceed to checkout
function buyItems() {
    if (cart.length === 0) {
        terminalOutput.textContent += 'Cart is empty. Add items to the cart before buying.\n';
        return;
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    window.location.href = 'checkout.html';
}

// Clear terminal output
function clearTerminal() {
    terminalOutput.textContent = '';
}

// Search products by name
function searchProducts(query) {
    const results = products.filter(p => p.title.toLowerCase().includes(query.toLowerCase()));
    if (results.length === 0) {
        terminalOutput.textContent += 'No products found.\n';
        return;
    }
    terminalOutput.innerHTML = 'Search Results:\n';
    results.forEach(product => {
        terminalOutput.innerHTML += `${product.title} - $${product.price}\n`;
    });
}

// Sort products by price or name
function sortProducts(criteria) {
    if (criteria === 'price') {
        products.sort((a, b) => a.price - b.price);
    } else if (criteria === 'name') {
        products.sort((a, b) => a.title.localeCompare(b.title));
    } else {
        terminalOutput.textContent += 'Invalid sort criteria. Use "price" or "name".\n';
        return;
    }
    displayProductsOnScreen();
}

// Event listener for terminal input
terminalInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleInput(terminalInput.value);
    }
});

// Initial fetch of products
fetchProducts();
