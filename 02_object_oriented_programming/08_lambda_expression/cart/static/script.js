// Wait for the page to fully load
document.addEventListener('DOMContentLoaded', function () {
    // Select all checkboxes for products and the element to display the total
    const productCheckboxes = document.querySelectorAll('.product-checkbox');
    const totalDisplay = document.getElementById('total');

    // Add event listener to each checkbox to update the total when clicked
    for (let i = 0; i < productCheckboxes.length; i++) {
        productCheckboxes[i].addEventListener('change', calculateAndUpdateTotal);
    }

    // Function to calculate and update the total cost based on selected products
    async function calculateAndUpdateTotal() {
        // Initialize an empty array to store IDs of selected products
        const selectedProductIds = [];

        // Loop through each checkbox to check if it's selected
        for (let i = 0; i < productCheckboxes.length; i++) {
            if (productCheckboxes[i].checked) {
                // If checked, add the product ID to the array
                selectedProductIds.push(productCheckboxes[i].getAttribute('data-id'));
            }
        }

        // Make a request to the server to get the total cost of selected products
        try {
            const response = await fetch(`/calculate_total?selected_ids[]=` + selectedProductIds.join('&selected_ids[]='), {
                method: 'GET'
            });

            const data = await response.json(); // Parse the response as JSON
            // Update the total display element with the calculated total from the server
            totalDisplay.textContent = data.total;
        } catch (error) {
            console.error('Error fetching total:', error);
        }
    }
});
